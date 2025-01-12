import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;

class Solution92334 {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        HashMap<String, Integer> idIndex = new HashMap<>();
        HashMap<String, List<String>> reportHashMap = new HashMap<>();
        
        for (int i = 0; i < id_list.length; i++) {
            idIndex.put(id_list[i], i);
            reportHashMap.put(id_list[i], new ArrayList<>());
        }
        
        for (String r : report) {
            String[] part = r.split(" ");
            List<String> reporters = reportHashMap.get(part[1]);
            if (!reporters.contains(part[0])) { // 신고자가 동일인에게 중복 신고하지 않도록
                reporters.add(part[0]);
            }
        }

        // 신고된 횟수 계산
        for (String id : reportHashMap.keySet()) {
            if (k <= reportHashMap.get(id).size()) {
                for (String reporter : reportHashMap.get(id)) {
                    answer[idIndex.get(reporter)]++;
                }
            }
        }
        
        return answer;
    }
}