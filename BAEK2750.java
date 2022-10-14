import java.util.Scanner;

public class BAEK2750 {

	public static void main(String[] args) {
		int N, j;
		Scanner in = new Scanner(System.in);
		N = in.nextInt();
		int[] arr = new int[N];
		for(int i=0; i<N; i++) {
			arr[i] = in.nextInt();
		}
		
		int temp = 0;
		for(int i=1; i<N; i++) {
			temp = arr[i];
			
			for(j=i-1; j>= 0 && arr[j] > temp; j--) {
				arr[j+1] = arr[j];
			}
			arr[j+1] = temp;
		}
		for(int i=0; i<N; i++) {
			System.out.println(arr[i]);
		}
	}

}
