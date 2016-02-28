/**
 * Created by Marshall Humble on 12/21/15.
 *
 * Project Euler Problem 6: Sum square Difference
 *
 * The sum of the squares of the first ten natural numbers is,
 * 12 + 22 + ... + 102 = 385
 * The square of the sum of the first ten natural numbers is,
 * (1 + 2 + ... + 10)2 = 552 = 3025
 * Hence the difference between the sum of the squares of the first ten natural numbers and the
 * square of the sum is 3025 − 385 = 2640.
 * Find the difference between the sum of the squares of the first one hundred natural numbers
 * and the square of the sum.
 *
 * 25164150
 * execution took 26 ms
 */

def benchmark = { closure ->
	start = System.currentTimeMillis()
	closure.call()
	now = System.currentTimeMillis()
	now - start
}

/*sum of squares of 100 numbers
* 1/3 n^3 + 1/2n^2 + 1/6n
* */

num = 100
sumOfSquare = (1/3 * (num**3)) + (1/2 * (num**2)) + (1/6 * (num))

squareOfSum = ((1..num).sum())**2
answer = sumOfSquare - squareOfSum
println(answer.abs().toInteger())



def duration = benchmark {
	(0..10000).inject(0) { sum, item ->
		sum + item
	}
}
println "execution took ${duration} ms"