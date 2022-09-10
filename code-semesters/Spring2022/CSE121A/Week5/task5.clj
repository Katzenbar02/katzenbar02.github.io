(defn decode-prime-list
    ([elements] (decode-prime-list elements 2 nil))
    ([elements counter accumulator]
        (let [first (first elements)
        incr (if (= firste 0) 1 firste)
        prepended-accumulator
        (if (= firste 1)
        (conj accumulator counter)
        accumulator)]
        (if (empty? (rest elements))
        (reverse prepended-accumulator)
        (recur (rest elements) (+ incr counter) prepended-accumulator)))))

(defn -main []
    (def primes '(2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97))
    (def rleprimes '(1 1 0 1 0 1 3 1 0 1 3 1 0 1 3 1 5 1 0 1 5 1 3 1 0 1 3 1 5 1 5 1 0 1 5 1 3 1 0 1 5 1 3 1 5 1 7 1 3))
    (println rleprimes)
    (println primes)
    (println (= primes (decode-prime-list rleprimes))))