import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String text = sc.nextLine();
        int result = 0;
        for (int i=0; i<text.length();i++) {
            float tmp;
            tmp = (float) text.charAt(i) - 65;
            if (tmp < 18) {
                if (tmp % 3 != 0) {
                    tmp -= 0.5;
                }
                result += 3 + (tmp / 3);
            } else if (tmp < 23) {
                tmp -= 1;
                result += 3 + (tmp /3);
            } else {
                result += 10;
            }
        }
        System.out.println(result);


    }
}
