import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int cnt = 0;
        for (int i = 1; i <= N; i++) {
            if (i >= 100) {
                int num1 = i / 100;
                int num2 = (i % 100) / 10;
                int num3 = i % 10;
                if((num1-num2) == (num2-num3)) {
                    cnt ++;
                }
        } else {
                cnt ++;
            }
        }
        System.out.println(cnt);
    }
}
