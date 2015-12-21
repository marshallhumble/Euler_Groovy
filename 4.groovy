/**
  * Created by Marshall Humble on 12/21/15.
  *
  * Project Euler Problem 4
  * A palindromic number reads the same both ways. The largest palindrome made from the product of two
  * 2-digit numbers is 9009 = 91 × 99.
  *
  * Find the largest palindrome made from the product of two 3-digit numbers.
  *
  * 906609
  * execution took 10 ms
  */

def benchmark = { closure ->
	start = System.currentTimeMillis()
	closure.call()
	now = System.currentTimeMillis()
	now - start
}


iPalindromeI = []

(100..999).each { x ->
	(100..999).each { y ->
		canidate = x * y
		canidateList = (canidate as String) as List
		if (canidateList == canidateList.reverse()) iPalindromeI << canidate
	}
}

println iPalindromeI.max()

def duration = benchmark {
	(0..10000).inject(0) { sum, item ->
		sum + item
	}
}
println "execution took ${duration} ms"

