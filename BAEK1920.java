import java.util.Arrays;
import java.util.Scanner;

public class BAEK1920 {

	public static void main(String[] args) {
		int N;
		Scanner in = new Scanner(System.in);
		N = in.nextInt();
		
		int [] arr = new int[N];
		
		for(int i=0; i<N; i++) {
			arr[i] = in.nextInt();
		}
		Arrays.sort(arr);
		
		int M;
		M = in.nextInt();
		StringBuilder sb = new StringBuilder();
		for(int i=0; i<M; i++) {
			if(binarySearch(arr, in.nextInt()) >=0) {
				sb.append(1).append('\n');
			}
			else {
				sb.append(0).append('\n');
			}
		}
		System.out.println(sb);

	}
	public static int binarySearch(int[] arr, int key) {
		int start = 0;
		int last = arr.length-1;
		
		while(start <= last) {
			int mid = (start+last)/2;
			if(arr[mid] > key) {
				last = mid -1;
			}
			else if(arr[mid] < key) {
				start = mid +1;
			}
			else if(arr[mid] == key) {
				return mid;
			}
		}
		return -1;
	}
}
