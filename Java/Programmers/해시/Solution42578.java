import java.util.HashMap;

class Solution42578 {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> clothesMap = new HashMap<>();
        for (String[] c : clothes) {
            String clothesType = c[1];
            clothesMap.put(clothesType, clothesMap.getOrDefault(clothesType, 0) + 1);
        }
        for (int cnt : clothesMap.values()) {
            answer *= (cnt+1);
        }
        return answer-1;
    }

    public static void main(String[] args) {
        Solution42578 s = new Solution42578();
        String[][] clothes = {
            {"yellow_hat", "headgear"},
            {"blue_sunglasses", "eyewear"},
            {"green_turban", "headgear"}
        };
        int result = s.solution(clothes);
        System.out.println(result);
    }
}