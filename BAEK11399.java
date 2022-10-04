import java.util.Arrays;
import java.util.Scanner;

public class BAEK11399 {

	public static void main(String[] args) {
		int N;
		Scanner in = new Scanner(System.in);
		N = in.nextInt();
		
		int[]p = new int[N];
		
		for(int i=0; i<N; i++) {
			p[i]=in.nextInt();
		}
		
		int sum=0;
		int result=0;
		Arrays.sort(p);
		for(int value : p) {
			sum +=value;
			result += sum;
		}
		System.out.println(result);

	}

}
