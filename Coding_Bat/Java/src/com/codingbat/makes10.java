package com.codingbat;

/**
 * Created by marshallhumble on 6/8/16.
 * Given 2 ints, a and b, return true if one if them is 10 or if their sum is 10.
 *
 */

public class makes10 {
    public boolean makes10(int a, int b) {
        return (a + b == 10) || (a == 10) || (b == 10);
    }

}
