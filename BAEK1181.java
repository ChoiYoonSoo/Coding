import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class BAEK1181 {

	public static void main(String[] args) throws IOException {
		int N;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		String[] ch = new String[N];
		
		for(int i=0; i<N; i++) {
			ch[i] = br.readLine();
		}
		
		Arrays.sort(ch,new Comparator<String>() {
			public int compare(String s1, String s2) {
				if(s1.length() == s2.length()) {
					return s1.compareTo(s2);
				}
				else {
					return s1.length() - s2.length();
				}
			}
		});
		
		StringBuilder sb = new StringBuilder();
		sb.append(ch[0]).append('\n');
		
		for(int i= 1; i<N; i++) {
			if(!ch[i].equals(ch[i-1])) {
				sb.append(ch[i]).append('\n');
			}
		}
		System.out.println(sb);
		
	}

}
