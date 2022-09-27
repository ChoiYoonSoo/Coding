import java.util.Scanner;

public class BAEK11047 {

	public static void main(String[] args) {
		int n,k,a,m = 0;
		int cnt = 0;
		int money[] = new int[10];
		Scanner scan = new Scanner(System.in);
		
		n = scan.nextInt();
		k = scan.nextInt();
		
		for(int i=0; i<n; i++) {
			money[i] = scan.nextInt();
		}
		
		while(k != 0) {
			for(int i=0; i<n; i++) {
				if(money[i] <= k) {
					m = money[i];
				}
			}
			a = k/m;
			cnt += a;
			k = k - (m*a);
		}
		System.out.println(cnt);
	}

}
