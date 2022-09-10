(defn cartesian-product
    ([] '(()))
    ([xs & more]
        (mapcat #(map (partial cons %)
        (apply cartesian-product more))
        xs)))

(def flavors1 ["Vanilla" "Chocolate" "Cherry-Ripple"])

(def flavors2 ["Lemon" "Butterscotch" "Licorice-Ripple"])

(def all-flavors (concat flavors1 flavors1))

(defn -main []
    (println "Two Lists Results: ")
    (println
        (filter
            #(= (first %) "Chocolate")
            (cartesian-product flavors1 flavors2)))
            (newline)
            (println "Single List Rsults: ")
            (println
            (filter
            #(or (= (first %) "Chocolate") (= (last %) "Chocolate"))
            (cartesian-product all-flavors all-flavors))))

(-main)