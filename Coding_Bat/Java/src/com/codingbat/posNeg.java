package com.codingbat;

/**
 * Created by marshallhumble on 6/8/16.
 */
public class posNeg {
    public boolean posNeg(int a, int b, boolean negative) {
        if (negative) {
            return a < 0 && b < 0;
        } else {
            return a < 0 && b > 0 || a > 0 && b < 0;
        }
    }
}