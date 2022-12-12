import java.util.Scanner;

public class BAEK2193 {

	public static void main(String[] args) {
		int N;
		Scanner in = new Scanner(System.in);
		N = in.nextInt();
		long[] arr = new long[N+1];
		
		arr[0] = 0;
		arr[1] = 1;
		
		for(int i=2; i<=N; i++) {
			arr[i] = arr[i-1] + arr[i-2];
		}
		
		System.out.println(arr[N]);

	}

}
