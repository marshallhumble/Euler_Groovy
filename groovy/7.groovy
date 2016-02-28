import com.sun.xml.internal.bind.v2.TODO
import groovyjarjarantlr.collections.List

/**
 * Created by Marshall Humble on 12/21/15.
 *
 * Project Euler Problem 7: 10001st prime
 *
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 * What is the 10 001st prime number?
 *
 */

//start timing
def benchmark = { closure ->
    start = System.currentTimeMillis()
    closure.call()
    now = System.currentTimeMillis()
    now - start
}


//Sieve of Eratosthenes
def sievePrimes = { bound ->
    def isPrime  = new BitSet(bound)
    isPrime[0..1] = false
    isPrime[2..bound] = true
    (2..(Math.sqrt(bound))).each { pc ->
        if (isPrime[pc]) {
            ((pc**2)..bound).step(pc) { isPrime[it] = false }
        }
    }
    (0..bound).findAll { isPrime[it] }
}





//end timing code
def duration = benchmark {
    (0..10000).inject(0) { sum, item ->
        sum + item
    }
}
println "execution took ${duration} ms"
