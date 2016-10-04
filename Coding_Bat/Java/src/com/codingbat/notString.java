package com.codingbat;


import java.util.Objects;

/**
 * Created by marshallhumble on 6/10/16.
 */
public class notString {
    public String notString(String str) {
        if (str.length() >= 3 && str.substring(0, 3).equals("not"))
            return str;
        return "not " + str;
    }
}
