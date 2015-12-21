/**
 * Created by Marshall Humble on 12/21/15.
 */

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
