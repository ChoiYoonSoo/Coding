import java.util.Scanner;
import java.util.StringTokenizer;

public class BAEK1541 {

	public static void main(String[] args) {
		int sum = Integer.MAX_VALUE;
		int temp;
		
		Scanner in = new Scanner(System.in);
		StringTokenizer st = new StringTokenizer(in.nextLine(),"-");
		
		while(st.hasMoreTokens()) {
			temp = 0;
			StringTokenizer s = new StringTokenizer(st.nextToken(),"+");
			
			while(s.hasMoreTokens()) {
				temp+=Integer.parseInt(s.nextToken());
			}
			
			if(sum == Integer.MAX_VALUE) {
				sum = temp;
			}
			else {
				sum -=temp;
			}
			
		}
		
		System.out.println(sum);
	}

}
