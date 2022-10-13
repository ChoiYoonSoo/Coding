import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BAEK2108 {

	public static void main(String[] args) throws IOException {
		int N;
		double sum = 0.0;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		int []arr = new int[N];
		StringBuilder sb = new StringBuilder();
		
		for(int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
			sum += arr[i];
		}
		
		Arrays.sort(arr);
		int mid = N/2;
		int minus = arr[N-1] - arr[0];
	
		int cnt = 0;
		int temp = -1;
		int idx = arr[0];
		boolean check = false;
		
		for(int i=0; i<N-1; i++) {
			if(arr[i] == arr[i+1]) {
				cnt++;
			}
			else {
				cnt = 0;
			}
			
			if(temp < cnt) {
				temp = cnt;
				idx = arr[i];
				check = true;
			}
			else if(temp == cnt && check == true) {
				idx = arr[i];
				check = false;
			}
		}
		
		sb.append(Math.round(sum/N)).append('\n').append(arr[mid]).append('\n').append(idx).append('\n').append(minus).append('\n');
		
		System.out.println(sb);
	}

}
