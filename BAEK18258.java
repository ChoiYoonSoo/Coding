import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BAEK18258 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		int last = 0;
		int cnt = 0;
		
		Queue<Integer> q = new LinkedList<>();
		StringTokenizer st;
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine()," ");
			String str = st.nextToken();
		
			if(str.equals("push")) {
				str = st.nextToken();
				q.add(Integer.parseInt(str));
				last = Integer.parseInt(str);
				
			}
			else if(str.equals("front")) {
				if(q.isEmpty()) {
					sb.append("-1").append("\n");
				}
				else {
					sb.append(q.peek()).append("\n");	
				}
			}
			else if(str.equals("back")) {
				if(q.isEmpty()) {
					sb.append("-1").append("\n");
				}
				else {
					sb.append(last).append("\n");
				}
			}
			else if(str.equals("empty")) {
				if(q.isEmpty()) {
					sb.append("1").append("\n");
				}
				else {
					sb.append("0").append("\n");
				}
			}
			else if(str.equals("size")) {
				sb.append(q.size()).append("\n");
			}
			else if(str.equals("pop")) {
				if(q.isEmpty()) {
					sb.append("-1").append("\n");
				}
				else {
					sb.append(q.poll()).append("\n");
				}
			}
		}

		System.out.println(sb);
	}

}
