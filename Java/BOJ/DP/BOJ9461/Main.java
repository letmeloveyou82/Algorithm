package BOJ.DP.BOJ9461;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        long[] P = new long[101];
        P[1] = 1;
        P[2] = 1;
        P[3] = 1;
        P[4] = 2;
        P[5] = 2;

        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());

            if (N <= 5) {
                System.out.println(P[N]);
            } else {
                for (int j = 6; j < N + 1; j++) {
                    P[j] = P[j - 1] + P[j - 5];
                }
                System.out.println(P[N]);
            }
        }
    }
}