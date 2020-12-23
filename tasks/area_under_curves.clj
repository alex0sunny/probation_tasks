(def read-input #(read-string (str "(" (read-line) ")")))
(def a-list (read-input))
(def b-list (read-input))
(def LR (read-input))
(def L (float (first LR)))
(def R (float (second LR)))
(def step (float 0.001))

(defn f-part [x a-list b-list] 
    (reduce + (for [[a b] (map list a-list b-list)] 
                  (* a (nth (reductions * 1 (repeat x)) b)))))

(def f-polynome 
    (if-not (neg? (first b-list)) #(f-part % a-list b-list) 
        (if-not (pos? (last b-list)) 
            #(f-part (/ 1 %) (reverse a-list) (map - (reverse b-list)))
            (let [[b-left b-right] (split-with neg? b-list)
                  [a-left a-right] (split-at (count b-left) a-list)
                  [a-left b-left] [(reverse a-left) (map - (reverse b-left))]]
                #(+ (f-part % a-right b-right) (f-part (/ 1 %) a-left b-left))))))

(defn f-calc [f] 
    (* step (reduce + (for [x (range L (+ R step) step)] (f (f-polynome x))))))

(println (f-calc identity))
(println (f-calc #(* Math/PI % %)))
