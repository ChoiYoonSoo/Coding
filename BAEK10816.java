import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class BAEK10816 {

	public static void main(String[] args) throws IOException {
		int N, M, key;
		Scanner in = new Scanner(System.in);
		
		N = in.nextInt();
		int [] a = new int[N];
		
		for(int i=0; i<N; i++) {
			a[i] = in.nextInt();
		}
		
		Arrays.sort(a);
		StringBuilder sb = new StringBuilder();
		M = in.nextInt();
		
		for(int i=0; i<M; i++) {
			key = in.nextInt();
			sb.append(lower(a,key) - upper(a,key)).append(" ");
			
		}
		System.out.print(sb);
	}
	
	public static int upper(int[] a, int key) {
		int low = 0;
		int high = a.length;
		
		while(low < high) {
			int mid = (low + high) / 2;
			if(a[mid] >= key) {
				high = mid;
			}
			else{
				low = mid + 1;
			}
		}
		
		return low;
	}
	
	public static int lower(int[] a, int key) {
		int low = 0;
		int high = a.length;
		
		while(low < high) {
			int mid = (low + high) / 2;
			if(a[mid] > key) {
				high = mid;
			}
			else{
				low = mid + 1;
			}
		}
		
		return low;
	}

}
