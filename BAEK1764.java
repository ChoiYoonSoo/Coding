import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class BAEK1764 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int M = in.nextInt();
		
		HashMap<String,Integer> map = new HashMap<>();
		StringBuilder sb = new StringBuilder();
		String str;
		List<String> list = new ArrayList<String>();
		int cnt = 0;
		
		for(int i=0; i<N; i++) {
			map.put(in.next(),i);
		}
		
		for(int i=0; i<M; i++) {
			str = in.next();
			if(map.get(str) != null) {
				list.add(str);
				cnt++;
			}
		}
		
		Collections.sort(list);
		sb.append(cnt).append("\n");
		for(String s:list) {
			sb.append(s).append("\n");
		}
		System.out.println(sb);
		
		

	}

}
