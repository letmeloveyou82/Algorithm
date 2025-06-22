package BOJ.DP.BOJ11057;

import java.io.*;

public class Main {
    static final int MOD = 10007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] dp = new int[N+1][10];

        // 초기화
        for (int j = 0; j < 10; j++) {
            dp[1][j] = 1;
        }

        // 누적합 점화식 적용
        for (int i = 2; i <= N; i++) {
            dp[i][0] = dp[i-1][0];
            for (int j = 1; j < 10; j++) {
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD;
            }
        }

        int answer = 0;
        for (int j = 0; j < 10; j++) {
            answer = (answer + dp[N][j]) % MOD;
        }

        System.out.println(answer);
    }
    
}
