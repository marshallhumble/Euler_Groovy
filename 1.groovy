/**
 * Project Euler Problem 1:
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
 * The sum of these multiples is 23.
 *
 * Find the sum of all the multiples of 3 or 5 below 1000.
 *
 * 233168
 * execution took 13 ms
 */



def benchmark = { closure ->
	start = System.currentTimeMillis()
	closure.call()
	now = System.currentTimeMillis()
	now - start
}

println((1..<1000).findAll({ it % 3 == 0 || it % 5 == 0 }).sum())

def duration = benchmark {
	(0..10000).inject(0) { sum, item ->
		sum + item
	}
}
println "execution took ${duration} ms"

