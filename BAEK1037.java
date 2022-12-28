import java.util.Scanner;

public class BAEK1037 {

	public static void main(String[] args) {
		int N;
		Scanner in = new Scanner(System.in);
		N = in.nextInt();
		
		int []arr = new int[N];
		
		for(int i=0; i<N; i++) {
			arr[i] = in.nextInt();
		}
		
		int min = arr[0], max = arr[0];
		
		for(int i=0; i<N; i++) {
			if(arr[i] < min) {
				min = arr[i];
			}
			if(arr[i] > max) {
				max = arr[i];
			}
		}
		
		System.out.println(min*max);

	}

}
