import java.util.*;

class Solution42628 {
    public int[] solution(String[] operations) {
        Queue<Integer> minHeap = new PriorityQueue<>();
        Queue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        
        for (String op : operations) {
            if (op.startsWith("I ")) {
                int num = Integer.parseInt(op.substring(2));
                minHeap.offer(num);
                maxHeap.offer(num);
            } else if (!minHeap.isEmpty() && op.equals("D -1")) {
                maxHeap.remove(minHeap.poll());
            } else if (!maxHeap.isEmpty() && op.equals("D 1")) {
                minHeap.remove(maxHeap.poll());
            }
        }
        
        if (minHeap.isEmpty() && maxHeap.isEmpty()) {
            return new int[]{0, 0};
        }
        
        return new int[]{maxHeap.poll(), minHeap.poll()};
    }
    
    public static void main(String[] args) {
        Solution42628 s = new Solution42628();
        String[] operations = {"I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"};
        int[] result = s.solution(operations);
        System.out.println(Arrays.toString(result));
    }
}