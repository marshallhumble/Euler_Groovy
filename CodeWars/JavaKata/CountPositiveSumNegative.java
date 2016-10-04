/**
 * Created by marshallhumble on 9/29/16.
 */

public class CountPositiveSumNegative {
    public static void main(String[] args) {
        System.out.print(countPositivesSumNegatives(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15}));
    }

    public static int[] countPositivesSumNegatives(int[] input) {
        int positiveCount = 0, negativeSum = 0;

        if (input == null || input.length == 0) {
            return new int[0];
        }

        for (int number : input) {
            if (number > 0) {
                positiveCount += 1;
            } else {
                negativeSum += number;
            }
        }

        return new int[]{positiveCount, negativeSum};
    }
}
