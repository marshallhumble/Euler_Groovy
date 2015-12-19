/*
 *`it` is an implicit parameter corresponding to the current element, while `i` is the index
 *So we can use a range, specify an or statement then sum & print the total.
 */


println((1..<1000).findAll({ it % 3 == 0 || it % 5 == 0 }).sum())
