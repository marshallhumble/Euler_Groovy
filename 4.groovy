/**
  * Created by Marshall Humble on 12/21/15.
  *
  * Project Euler Problem 4
  * A palindromic number reads the same both ways. The largest palindrome made from the product of two
  * 2-digit numbers is 9009 = 91 × 99.
  *
  * Find the largest palindrome made from the product of two 3-digit numbers.
  */

iPalindromeI = []

(100..999).each { x ->
	(100..999).each { y ->
		canidate = x * y
		canidateList = (canidate as String) as List
		if (canidateList == canidateList.reverse()) iPalindromeI << canidate
	}
}

println iPalindromeI.max()


