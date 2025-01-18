package Programmers.자료구조;

import java.util.HashSet;
import java.util.Set;

class Solution77484 {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int unknownCnt = 0;
        int correctCnt = 0;
        
        Set<Integer> winSet = new HashSet<>();
        for (int num : win_nums) {
            winSet.add(num);
        }
        
        for (int lotto : lottos) {
            if (lotto == 0) {
                unknownCnt++;
            } else if (winSet.contains(lotto)) {
                correctCnt++;
            }
        }
        
        answer[1] = 7-Math.max(correctCnt, 1);
        answer[0] = 7-Math.max(correctCnt+unknownCnt, 1);
        
        return answer;
    }
}