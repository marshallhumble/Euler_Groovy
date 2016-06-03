package com.codingbat;


/**
 * Created by mhumble on 6/3/16.
 */
public class diff21 {
    public int diff21(int n) {
        if (n > 21) {
            return 2 * java.lang.StrictMath.abs(n - 21);
        } else {
            return java.lang.StrictMath.abs(n - 21);
        }
    }

}



