import java.util.Arrays;
import java.util.Scanner;

public class BAEK2587 {

	public static void main(String[] args) {
		int N = 5;
		int avg = 0;
		int mid = 0;
		int []arr = new int[5];
		Scanner in = new Scanner(System.in);
		
		for(int i = 0; i<5; i++) {
			arr[i] = in.nextInt();
			avg += arr[i];
		}
		avg = avg / 5;
		
		Arrays.sort(arr);
		mid = arr[arr.length/2];
		System.out.println(avg);
		System.out.println(mid);

	}

}
