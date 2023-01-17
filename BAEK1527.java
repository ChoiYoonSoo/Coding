import java.util.Scanner;

public class BAEK1527 {
	static int a,b;
	static int cnt = 0;

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		a = in.nextInt();
		b = in.nextInt();
		
		dfs(0);
		
		System.out.println(cnt);
	}
	
	public static void dfs(long num) {
		if(num > b)
			return;
		
		if(a <= num && b >= num) {
			cnt++;
		}
		dfs(num*10+4);
		dfs(num*10+7);
	}

}
