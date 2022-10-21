import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class BAEK9012 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		Stack<Character> stack = new Stack<Character>();
		StringBuilder sb = new StringBuilder();
		
		for(int i=0; i<n; i++) {
			String str = br.readLine();
			
			for(int j=0; j<str.length(); j++) {
				if(str.charAt(j) == '(') {
					stack.push(str.charAt(j));
				}
				else {
					if(stack.isEmpty()) {
						stack.push(str.charAt(j));
					}
					else if(stack.peek() == '(') {
						stack.pop();
					}
					else
						break;
				}
			

			}
			if(stack.isEmpty()) {
				sb.append("YES").append('\n');	
			}
			else {
				sb.append("NO").append('\n');
			}
			stack.clear();
		}
		
		System.out.println(sb);
	}

}
