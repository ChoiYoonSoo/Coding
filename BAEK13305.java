import java.util.Scanner;

public class BAEK13305 {

	public static void main(String[] args){
		int N;
		long result = 0;
		
		Scanner in = new Scanner(System.in);
		N = in.nextInt();
		
		long []city = new long[N];
		long []oil = new long[N-1];
		
		for(int i=0; i<N-1; i++) {
			oil[i] = in.nextInt();
		}
		
		for(int i=0; i<N; i++) {
			city[i] = in.nextInt();
		}
		
		for(int i=0; i<N-2; i++) {
			if(city[i] < city[i+1]) {
				city[i+1] = city[i];
			}
		}
		for(int i=0; i<N-1; i++) {
			result += city[i] * oil[i];
		}
		System.out.println(result);

	}

}
