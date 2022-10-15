import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class BAEK10815 {

	public static void main(String[] args) throws IOException {
		int N,M,num;
		int cnt = 0;
		Scanner in = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		N = in.nextInt();
		int []arr = new int[N];
		
		for(int i=0; i<N; i++) {
			arr[i] = in.nextInt();
		}
		Arrays.sort(arr);
		M = in.nextInt();
		for(int i=0; i<M; i++) {
			num = in.nextInt();
			
			if(binarySearch(arr,num) == true) {
				sb.append('1').append(" ");
			}
			else {
				sb.append('0').append(" ");
			}
				
		}
		
		System.out.println(sb);

	}
	
	public static Boolean binarySearch(int []arr, int N) {
		int start = 0;
		int end = arr.length-1;
		int mid = 0;
		Boolean check = false;
		
		while(start <= end) {
			mid = (start+end)/2;
			
			if(arr[mid] == N) {
				check = true;
				return check;
			}
			else if(arr[mid] < N) {
				start = mid +1;
			}
			else
				end = mid-1;
		}
		return check;
	}

}
