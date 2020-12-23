;; Definite Integrals via Numerical Methods
;; This relates to definite integration via numerical methods.
;; Consider the algebraic expression given by:
;; a1 * x^b1 + a2 * x^b2 + a3 * x^b3 ... an * x^bn
;; For the purpose of numerical computation, the area under the curve between the limits and
;; can be computed by the Limit Definition of a Definite Integral.
;; Here is some background about areas and volume computation.

;; Using equal subintervals of length = 0.001, you need to:
;;     Evaluate the area bounded by a given polynomial function of the kind described above,
;; between the given limits of L and R.
;; and
;;     Evaluate the volume of the solid obtained by revolving this polynomial curve around the
;; x-axis.

;; A relative error margin of 0.01 will be tolerated.

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
