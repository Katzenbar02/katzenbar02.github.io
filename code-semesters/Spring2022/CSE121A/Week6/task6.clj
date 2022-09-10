(defn cartesian-product
    ([] '(()))
    ([xs & more]
        (mapcat #(map (partial cons %)
        (apply cartesian-product more))
        xs)))

(def firstnames ["John" "Jane" "Mary" "Bob" "Tom"])

(def lastnames '("Smith" "Jones" "Williams" "Brown" "Davis"))

(def firstnames-lastnames (concat firstnames lastnames))
(defn -main []
    (println firstnames)
    (println lastnames)
    (println "First name: ")
    (println
        (filter
            #(= (first %) "Smith")
            (cartesian-product firstnames lastnames)))
            (newline)
            (println "Last name: ")
            (println
            (filter
            #(or (= (first %) "Smith") (= (last %) "Smith"))
            (cartesian-product firstnames-lastnames firstnames-lastnames))))


(-main)