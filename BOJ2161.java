import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ2161 {

	public static void main(String[] args) {
		int N;
		Scanner in = new Scanner(System.in);
		N = in.nextInt();
		
		Queue<Integer> q = new LinkedList<>();

		
		for(int i=0; i<N; i++) {
			q.add(i+1);
		}
		
		while(q.size() > 1) {
			System.out.print(q.poll()+" ");
			q.add(q.poll());
		}
		System.out.println(q.poll());
	}

}
