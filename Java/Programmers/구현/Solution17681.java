class Solution17681 {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        for (int i = 0; i < n; i++) {
            int combined = arr1[i] | arr2[i];
            String binary = String.format("%16s", Integer.toBinaryString(combined));
            binary = binary.substring(binary.length()-n);
            binary = binary.replace("1", "#").replace("0", " ");
            answer[i] = binary;
        }
        return answer;
    }
}