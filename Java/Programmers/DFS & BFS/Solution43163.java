import java.util.*;

class Solution43163 {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        if (!Arrays.asList(words).contains(target)) {
            return answer;
        }
        
        boolean[] visited = new boolean[words.length];
        Queue<String[]> q = new LinkedList<>();
        q.add(new String[]{begin, "0"});
        
        while (!q.isEmpty()) {
            String[] current = q.poll();
            String word = current[0];
            int cnt = Integer.parseInt(current[1]);
            
            if (word.equals(target)) {
                answer = cnt;
                break;
            }
            
            for (int i=0;i<words.length;i++) {
                int diffCnt = 0;
                if (!visited[i]) {
                    for (int j=0;j<word.length();j++) {
                        if(word.charAt(j) != words[i].charAt(j)) {
                            diffCnt++;
                        }
                    }
                    if (diffCnt == 1) {
                        q.add(new String[]{words[i], Integer.toString(cnt+1)});
                        visited[i] = true;
                    }
                }
            }
        }
        return answer;
    }
    
    public static void main(String[] args) {
        Solution43163 sol = new Solution43163();
        String begin = "hit";
        String target = "cog";
        String[] words = {"hot", "dot", "dog", "lot", "log", "cog"};
        System.out.println(sol.solution(begin, target, words));  // 예상 출력: 4
    }
}