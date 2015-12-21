/**
 * Created by mhumble on 12/21/15.
 *
 * Project Euler Problem 5: Smallest multiple
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 *
 * 232792560
 * execution took 9 ms
 */

def benchmark = { closure ->
	start = System.currentTimeMillis()
	closure.call()
	now = System.currentTimeMillis()
	now - start
}

divisor = (2..19)
canidate = 20

while (divisor.find({ divisor -> canidate % divisor != 0 })) { canidate += 20 } //add by 20 to reduce the execution time
println canidate

def duration = benchmark {
	(0..10000).inject(0) { sum, item ->
		sum + item
	}
}
println "execution took ${duration} ms"

