import java.util.Scanner;

public class BAEK11726 {
	public static void main(String[] args) {
		int N;
		int sum = 0;
		Scanner in = new Scanner(System.in);
		
		N = in.nextInt();
		int []arr = new int[N+2];
		
		arr[1] = 1;
		arr[2] = 2;
		for(int i=3; i<=N; i++) {
			arr[i]= arr[i-1] + arr[i-2]%10007;
		}
		System.out.println(arr[N]%10007);
	}
}
