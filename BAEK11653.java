import java.util.Scanner;

public class BAEK11653 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int N = in.nextInt();
		
		for(int i=2; i<=N; i++) {
			while(N % i == 0) {
				N /= i;
				sb.append(i).append("\n");
			}
		}
		
		System.out.println(sb);

	}

}
