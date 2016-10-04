import java.util.*;
import java.util.stream.*;

public class HighAndLow {
    private static String HighAndLow(String numbers) {
        String[] array = numbers.split(" ");
        List<Integer> nums = new ArrayList<>();

        for(String i : array){
            nums.add(Integer.parseInt(i));
        }

        return Collections.max(nums) + " " + Collections.min(nums);
    }

    public static void main(String[] args) {
        System.out.println(HighAndLow("-1 -1"));
        System.out.println(HighAndLow("42"));
        System.out.println(HighAndLow("1 1"));
        System.out.println(HighAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4"));
        System.out.println(HighAndLow("1 2 3 4 5"));
        System.out.println(HighAndLow("1 2 -3 4 5"));
        System.out.println(HighAndLow("1 9 3 4 -5"));
    }
}