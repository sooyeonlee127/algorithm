import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int tc = 0; tc < T; tc++) {
            int N = sc.nextInt();
            String text = sc.next();
            for (int i=0; i < text.length(); i++) {
                for (int j=0; j < N; j++) {
                    System.out.print(text.charAt(i));
                }
            }
            System.out.print("\n");
        }

    }

}

