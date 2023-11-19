import java.io.*;
import java.util.StringTokenizer;

public class Main {
    final static int Red = 0;
    final static int Green = 1;
    final static int Blue = 2;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[][] cost = new int[N][3];

        for(int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine(), " ");
            cost[i][Red] = Integer.parseInt(st.nextToken());
            cost[i][Green] = Integer.parseInt(st.nextToken());
            cost[i][Blue] = Integer.parseInt(st.nextToken());
        }
        
        // 1부터 N-1까지 각 i별 i-1의 서로 다른 색상 중 최솟값을 누적하여 더한다.
        for(int i=1;i<N;i++){
            cost[i][Red] += Math.min(cost[i-1][Green], cost[i-1][Blue]);
            cost[i][Green] += Math.min(cost[i-1][Red], cost[i-1][Blue]);
            cost[i][Blue] += Math.min(cost[i-1][Red], cost[i-1][Green]);
        }

        int result = Math.min(Math.min(cost[N-1][Red], cost[N-1][Green]), cost[N-1][Blue]);
        System.out.println(result);
    }
}
