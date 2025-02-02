import java.util.ArrayList;

class Solution64061 {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int n = board.length;
        ArrayList<Integer> pick = new ArrayList<>();
        for (int move : moves) {
            move -= 1;
            for (int r = 0; r < n; r++) {
                if (board[r][move] != 0) {
                    if (!pick.isEmpty() && pick.get(pick.size() - 1) == board[r][move]) {
                        answer += 2;
                        pick.remove(pick.size() - 1);
                        board[r][move] = 0;
                        break;
                    }
                    pick.add(board[r][move]);
                    board[r][move] = 0;
                    break;
                }
            }
        }
        return answer;
    }
}