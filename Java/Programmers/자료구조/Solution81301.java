package Programmers.자료구조;

import java.util.HashMap;

class Solution81301 {
    public int solution(String s) {
        HashMap<String, Integer> h1 = new HashMap<>();
        h1.put("zero", 0);
        h1.put("one", 1);
        h1.put("two", 2);
        h1.put("three", 3);
        h1.put("four", 4);
        h1.put("five", 5);
        h1.put("six", 6);
        h1.put("seven", 7);
        h1.put("eight", 8);
        h1.put("nine", 9);
        
        // s에 h1에 있는 key가 있다면 바로 value 값으로 변경
        for (String key : h1.keySet()) {
            if (s.contains(key)) {
                s = s.replace(key, h1.get(key).toString());
            }
        }
        return Integer.parseInt(s);
    }
}