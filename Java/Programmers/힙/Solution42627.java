package Programmers.힙;

import java.util.*;

class Solution42627 {
    public int solution(int[][] jobs) {
        int answer = 0;
        Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]);
        PriorityQueue<int[]> waiting = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        int n = jobs.length;
        
        int idx = 0;
        int now = 0;
        int finishJobCnt = 0;
        while (finishJobCnt != n){
            while (idx < n && now >= jobs[idx][0]){
                waiting.add(jobs[idx++]);
            }
            
            if(!waiting.isEmpty()){
                int[] job = waiting.poll();
                answer += now - job[0] + job[1];
                now += job[1];
                finishJobCnt++;
            } else {
                now = jobs[idx][0];
            }
        }
        
        return answer / n;
    }

    public static void main(String[] args) {
        Solution42627 solution = new Solution42627();
        int[][] jobs = {{0, 3}, {1, 9}, {2, 6}};
        int result = solution.solution(jobs);
        System.out.println(result);
    }
}