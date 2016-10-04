package com.codingbat;

/**
 * Created by marshallhumble on 6/8/16.
 */
public class parrotTrouble {
    public boolean parrotTrouble(boolean talking, int hour) {
        return talking && (hour < 7 || hour > 20);
    }
}
