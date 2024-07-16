package BOJ.자료구조.BOJ10773;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

import java.util.Stack;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		Stack<Integer> stack = new Stack<>();
		int K = Integer.parseInt(br.readLine());

		for(int i = 0; i < K; i++) {
			int now = Integer.parseInt(br.readLine());
			if (now == 0) {
				stack.pop();
			}
			else {
				stack.push(now);
			}
		}

		int sum = 0;
		for(int o : stack) {
			sum += o;
		}

		System.out.println(sum);
	}
}