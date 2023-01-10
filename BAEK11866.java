import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BAEK11866 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int K = in.nextInt();
		
		Queue<Integer> q = new LinkedList<>();
		
		for(int i=0; i<N; i++) {
			q.add(i+1);
		}
		StringBuilder sb = new StringBuilder();
		
		while(q.size() > 1) {
			for(int i=0; i<K-1; i++) {
				q.add(q.poll());
			}
			sb.append(q.poll()).append(", ");
		}
		sb.append(q.poll()).append(">");
		
		System.out.println("<"+ sb);

	}

}
