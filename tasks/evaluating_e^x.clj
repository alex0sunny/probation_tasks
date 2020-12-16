;; The series expansion of e^x is given by:
;; 1 + x + x^2 / 2! + x^3 / 3! + ...
;; Evaluate e^x for given value of x by using the above expansion for the first 10 terms. 

(def x (Double/parseDouble (clojure.string/trim (read-line))))

(def result 2423600.1887)

(let [denominators  (reductions * 1. (rest (range)))
      numerators    (iterate #(* % x) 1.)
      items (map / numerators denominators)]
  (println (apply + (take 10 items))))
