import java.io.*;
import java.util.*;

public class Main {
    static int N; 
    static int[][] board;
    static boolean[][] visited;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        int maxRainfall = 0;

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                maxRainfall = Math.max(maxRainfall, board[i][j]);
            }
        }
        
        int result = 0;

        for (int h = 0; h < maxRainfall; h++) {
            visited = new boolean[N][N];
            int safeZoneCnt = 0;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N ; j++) {
                    // 잠기지 않은 영역이고 방문하지 않은 곳 BFS 탐색
                    if (board[i][j] > h && !visited[i][j]) {
                        bfs(i, j, h);
                        safeZoneCnt++;
                    }
                }
            }
            result = Math.max(result, safeZoneCnt);
        }

        System.out.println(result);
    }

    static void bfs(int startX, int startY, int rainfall) {
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{startX, startY});
        visited[startX][startY] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1];

            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                    if (board[nx][ny] > rainfall && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        q.add(new int[]{nx, ny});
                    }
                }
            }
        }
    }
}
