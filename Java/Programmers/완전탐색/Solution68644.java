import java.util.*;

class Solution68644 {
    public int[] solution(int[] numbers) {
        Set<Integer> answerSet = new HashSet<>();
        int n = numbers.length;
        
        for (int i = 0; i < n ; i++) {
            for (int j = i+1; j < n; j++) {
                answerSet.add(numbers[i]+numbers[j]);
            }
        }
        
        // Set -> List -> 정렬
        List<Integer> answerList = new ArrayList<>(answerSet);
        Collections.sort(answerList);
        
        // List -> int[] 배열로 변환
        return answerList.stream().mapToInt(Integer::intValue).toArray();
    }
}