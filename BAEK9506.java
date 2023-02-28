import java.util.Scanner;

public class BAEK9506 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int sum = 0;
		StringBuilder sb2 = new StringBuilder();
		
		while(true) {
			StringBuilder sb = new StringBuilder();
			int N = in.nextInt();
			sum = 0;
			if(N == -1) {
				break;
			}
			
			for(int i=1; i<N; i++) {
				if(N % i == 0) {
					sum += i;
					sb.append(i).append(" + ");
				}
			}
			if(sum == N) {
				sb.deleteCharAt(sb.length()-2);
				sb2.append(N).append(" = ").append(sb).append("\n");
			}
			else {
				sb2.append(N).append(" is NOT perfect.").append("\n");
			}
			
			
		}
		System.out.println(sb2);
		

	}

}
