import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int tc = 0; tc < T; tc ++) {
            int [] lst;
            int N = sc.nextInt();
            lst = new int[N];
            double total = 0;
            double cnt = 0;
            for (int i = 0; i < N; i ++) {
                int temp = sc.nextInt();
                lst[i] = temp;
                total += temp;
            }
            for (int j = 0; j < N; j ++) {
                if (lst[j] > total / N) {
                    cnt++;
                }
            }
            System.out.printf("%.3f%%\n" ,(cnt/N)*100);
        }
        sc.close();
    }
}
