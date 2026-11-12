
public class Bug3 {

    public static int calculateSum(int[] numbers) {
        int sum = 0;

        for (int i = 0; i <= numbers.length; i++) {
            sum += numbers[i];
        }

        return sum;
    }

    public static void main(String[] args) {
        int[] values = {10, 20, 30, 40};

        int result = calculateSum(values);

        System.out.println("Sum: " + result);
    }
}
