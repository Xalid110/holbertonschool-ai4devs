
public class Bug3Fixed {

    public static int calculateSum(int[] numbers) {
        int sum = 0;

        for (int i = 0; i < numbers.length; i++) {
            sum += numbers[i];
        }

        return sum;
    }

    public static void main(String[] args) {
        assert calculateSum(new int[]{10, 20, 30, 40}) == 100;
        assert calculateSum(new int[]{5}) == 5;
        assert calculateSum(new int[]{}) == 0;
        assert calculateSum(new int[]{-2, 2}) == 0;

        System.out.println("All bug3 tests passed!");
    }
}
