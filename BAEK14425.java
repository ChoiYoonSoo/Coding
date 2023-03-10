import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class BAEK14425 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		HashMap<String,Integer> map1 = new HashMap<>();
		HashMap<Integer,String> map2 = new HashMap<>();
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			map1.put(st.nextToken(),i);
		}
		
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			map2.put(i,st.nextToken());
		}
		
		int cnt = 0;
		for(int i=0; i<M; i++) {
			if(map1.containsKey(map2.get(i))) {
				cnt++;
			}
		}
		
		System.out.println(cnt);
		
	}

}
