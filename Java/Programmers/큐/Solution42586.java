import java.util.*;

class Solution42586 {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> result = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();
        
        for (int i = 0; i < progresses.length; i++) {
            int remaining = 100 - progresses[i];
            int days = (int) Math.ceil((double) remaining / speeds[i]);
            q.offer(days);
        }
        
        while (!q.isEmpty()) {
            int x = q.poll();
            int cnt = 1;
            
            while (!q.isEmpty() && q.peek() <= x) {
                q.poll();
                cnt++;
            }
            
            result.add(cnt);
        }
        
        
        int[] answer = result.stream().mapToInt(i -> i).toArray();
        
        return answer;
    }
    
    public static void main(String[] args) {
        Solution42586 sol = new Solution42586();
        int[] progresses = {93, 30, 55};
        int[] speeds = {1, 30, 5};

        int[] result = sol.solution(progresses, speeds);

        System.out.println("출력 결과: " + Arrays.toString(result));  // [2, 1]
    }
}