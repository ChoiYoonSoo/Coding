import java.util.Scanner;

public class BAEK2581 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int M, N;
		int sum = 0;
		int Prime = 0;
		
		M = in.nextInt();
		N = in.nextInt();
		int min = N;
		
		for(int i=M; i<=N; i++) {
			if(M==1) continue;
			Prime = 0;
			for(int j=2; j<i; j++) {
				if(i%j==0) {
					Prime = 1;
					break;
				}
			}
			if(Prime == 0) {
				sum += i;
				if(min > i) {
					min = i;
				}
			}
		}
		if(sum == 0) {
			System.out.println(-1);
		}
		else {
			System.out.println(sum);
			System.out.println(min);	
		}
		

	}

}
