import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class BAEK10828 {

	public static void main(String[] args) throws IOException{
		int N, num;
		String M;
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		Stack<Integer> stack = new Stack<Integer>();
		
		N = Integer.parseInt(br.readLine());
		
		for(int i=0; i<N; i++) {
			M = br.readLine();
			StringTokenizer st = new StringTokenizer(M);
			M = st.nextToken();
			if(M.equals("push")) {
				M = st.nextToken();
				num = Integer.parseInt(M);
				stack.push(num);
			}
			
			else if(M.equals("pop")) {
				if(stack.isEmpty() == false) {
					sb.append(stack.pop()).append("\n");
				}
				else
					sb.append("-1").append("\n");
			}
			
			else if(M.equals("size")) {
				sb.append(stack.size()).append("\n");
			}
			else if(M.equals("empty")) {
				if(stack.isEmpty() == true) {
					sb.append("1").append("\n");
				}
				else
					sb.append("0").append("\n");
			}
			else if(M.equals("top")) {
				if(stack.isEmpty() == false) {
					sb.append(stack.peek()).append("\n");
				}
				else
					sb.append("-1").append("\n");
			}
		}
		System.out.println(sb);
	}

}
