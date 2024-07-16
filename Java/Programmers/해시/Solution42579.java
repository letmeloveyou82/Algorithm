import java.util.*;

class Solution42579 {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        Map<String, List<int[]>> bestAlbum = new HashMap<>();
        Map<String, Integer> playCount = new HashMap<>();
        
        for(int i=0;i<genres.length;i++){
            bestAlbum.putIfAbsent(genres[i], new ArrayList<>());
            bestAlbum.get(genres[i]).add(new int[]{plays[i], i});
            playCount.put(genres[i], playCount.getOrDefault(genres[i], 0)+plays[i]);
        }
        
        List<Map.Entry<String, Integer>> playGenresDesc = new ArrayList<>(playCount.entrySet());
        playGenresDesc.sort((a, b) -> b.getValue() - a.getValue());
        
        for(Map.Entry<String, Integer> entry : playGenresDesc) {
            String genre = entry.getKey();
            List<int[]> playSongs = bestAlbum.get(genre);
            playSongs.sort((a, b) -> b[0] == a[0] ? a[1] - b[1] : b[0] - a[0]);
            
            if(playSongs.size() == 1){
                answer.add(playSongs.get(0)[1]);
            }
            else{
                answer.add(playSongs.get(0)[1]);
                answer.add(playSongs.get(1)[1]);
            }
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        Solution42579 sol = new Solution42579();
        String[] genres = {"classic", "pop", "classic", "classic", "pop"};
        int[] plays = {500, 600, 150, 800, 2500};
        int[] result = sol.solution(genres, plays);

        System.out.println(Arrays.toString(result));
    }
}