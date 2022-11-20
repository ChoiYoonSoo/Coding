import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BAEK6550 {

	public static void main(String[] args) throws IOException {
		String s;
		String t;
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int idx = 0;
		String str;
		
		while((str = br.readLine())!=null) {
			StringTokenizer st = new StringTokenizer(str);
			
			s = st.nextToken();
			t = st.nextToken();
			
			idx=0;
			
			for(int i=0; i<t.length(); i++) {
				if(s.charAt(idx) == t.charAt(i)) {
					idx++;
				}
				if(idx == s.length())
					break;
			}
			
			if(idx == s.length()) {
				System.out.println("Yes");
			}
			else
				System.out.println("No");
		}

	}

}
