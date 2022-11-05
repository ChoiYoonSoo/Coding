import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class BAEK10814 {

	public static void main(String[] args) throws IOException {
		int N;
		Scanner in = new Scanner(System.in);
		
		N = in.nextInt();
		String [][]info = new String [N][2];
		
		for(int i=0; i<N; i++) {
			info[i][0] = in.next();
			info[i][1] = in.next();
		}
		
		Arrays.sort(info,new Comparator<String[]>() {
			
			@Override
			public int compare(String[] s1, String[] s2) {
				return Integer.parseInt(s1[0]) - Integer.parseInt(s2[0]);
			}
		});
		
		for(int i=0; i<N; i++) {
			System.out.println(info[i][0] + " " + info[i][1]);
		}
		
	}

}
