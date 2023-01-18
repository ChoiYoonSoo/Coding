import java.util.Scanner;

public class BAEK1978 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int cnt = 0;
		
		for(int i=0; i<N; i++) {
			int num = in.nextInt();
			if(is_Prime(num)==true) {
				cnt++;
			}
		}
		System.out.println(cnt);

	}
	
	public static boolean is_Prime(int n) {
		if(n == 1) {
			return false;
		}
		
		for(int i=2; i<n; i++) {
			if(n%i == 0) return false;
		}
		return true;
		
	}

}
