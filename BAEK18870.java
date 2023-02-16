import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class BAEK18870 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		
		int [] origin = new int[N];
		int [] sorted = new int[N];
		
		for(int i=0; i<N; i++) {
			origin[i] = sorted[i] = in.nextInt();
		}
		
		HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
		StringBuilder sb = new StringBuilder();
		Arrays.sort(sorted);
		
		int cnt = 0;
		for(int v: sorted) {
			
			if(!map.containsKey(v)) {
				map.put(v, cnt);
				cnt++;
			}
		}
		
		for(int key: origin) {
			
			int value = map.get(key);
			sb.append(value).append(" ");
		}
		
		System.out.println(sb);
	}

}
