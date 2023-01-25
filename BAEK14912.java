import java.util.Scanner;

public class BAEK14912 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n;
		int d;
		
		n = in.nextInt();
		d = in.nextInt();
		int cnt = 0;
		for(int i=1; i<=n; i++) {
			int num = i;
			while(num>0) {
				if(num%10 == d) {
					cnt++;
				}
				num /= 10;
			}
		}
		
		System.out.println(cnt);

	}

}
