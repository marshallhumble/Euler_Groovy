/**
 * Created by Marshall Humble on 12/21/15.
 *
 * Project Euler Problem 3:
 *
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143 ?
 *
 * 6857
 * execution took 21 ms
 */

def benchmark = { closure ->
	start = System.currentTimeMillis()
	closure.call()
	now = System.currentTimeMillis()
	now - start
}

def searchNumber = 600851475143

def largestPrimeFactor = { BigInteger it, divisor = 1, factorList = [] ->
	while (it > 1) {
		divisor += 1
		while (it % divisor == 0) {
			factorList << divisor
			it /= divisor
		}
	}
	factorList.last()
}

println(largestPrimeFactor(searchNumber))


def duration = benchmark {
	(0..10000).inject(0) { sum, item ->
		sum + item
	}
}
println "execution took ${duration} ms"