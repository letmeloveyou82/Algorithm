package BOJ.Graph.BOJ5567;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int invite_num = 0; // 결혼식에 초대하는 동기 수
    public static ArrayList<Integer>[] graph; // 친구 관계 그래프
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        graph = new ArrayList[n+1];
        boolean[] visited = new boolean[n+1];

        for(int i=0; i <= n; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i=0;i<m;i++){
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
            graph[b].add(a);
        }

        visited[1] = true;
        dfs(1, 0, visited);

        // 상근이 제외하고 count라서 2부터
        for(int i=2;i<visited.length;i++){
            if(visited[i]){
                invite_num++;
            }
        }

        System.out.println(invite_num);
    }

    public static void dfs(int node, int depth, boolean[] visited) {
        if(depth == 2){
            return;
        }

        for(int i=0;i<graph[node].size();i++){
            int nextNode = graph[node].get(i);
            visited[nextNode] = true;
            dfs(nextNode, depth+1, visited);
        }
    }
}
