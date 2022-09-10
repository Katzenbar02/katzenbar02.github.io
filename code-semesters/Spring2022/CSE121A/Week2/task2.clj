(defn exercise-math []
    (def x 3)
    (def y 5)
    (def z 7)
    (println (+ x y z))
    (println (*x y z))
    (println (/ x y z))
    (println ( + (Math/pow x 2) (* y 3) z))
    (println (+ (Math/pow z x) (Math/pow x z)))
    (println (+ (/z y z)))

    (dec (* x y z)))

(defn exercise-logic []
    (def a 13)
    (def b 17)
    (def c 23)
    (println (> a b))
    (println (> b a))
    (println (< a b))
    (println (< b c))
    (println (>= c c))
    (println (= a c))
    (println (<= a b))
    (println (and (< a b) (> b c)))

    (or (< a b) (> b c))
)