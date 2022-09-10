(defn gcd [a b]
    (id (zero? b)
    a
    (recur b (mod a b))))

(defn gcd-instrumented [a b]
(if (zero? b)
a
(do
    (println a '= b (list (quot a b)) '+ (rem a b))
    (recur b (mod a b)))))

(defn gcd-no-recursion [a b]
    (last ; for the greatest
        (filter
            #(and (zero? (mod b %)) (zero? (mod a %)))
            (range 1 (inc (min a b))))))

(defn gcd-via-reduce []
    (loop [a (map #(Integer/parseInt %) ( clojure.string/split (read-line) #" "))]
        (cond
            (reduce > a) (recur (list (reduce - a) (last a)))
            (reduce < a) (recur (list (- (reduce - a)) (first a)))
            (reduce = a) (println (first a)))))

(gcd 234 66)

(gcd-instrumented 234 66)

(gcd-no-recursion 234 66)

(gcd-via-reduce)