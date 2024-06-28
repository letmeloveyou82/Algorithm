class Solution43165 {
    private int answer = 0;
    private void dfs(int[] numbers, int target, int idx, int val){
        if (idx >= numbers.length) {
            if (val == target){
                answer++;
            }
            return;
        }
        dfs(numbers, target, idx+1, val+numbers[idx]);
        dfs(numbers, target, idx+1, val-numbers[idx]);
    }
    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);
        return answer;
    }
    public static void main(String[] args) {
        Solution43165 s = new Solution43165();
        int[] numbers = {1, 1, 1, 1, 1};
        int target = 3; 
        int result = s.solution(numbers, target);
        System.out.println(result); 
    }
}