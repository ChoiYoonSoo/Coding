import java.util.Scanner;

public class BAEK24416 {
	static int[] f;
	static int cnt1 = 0, cnt2 = 0;
	public static void main(String[] args) {
		int N;
		Scanner in = new Scanner(System.in);
		N = in.nextInt();
		f = new int[N];
		fib(N);
		fibonacci(N);
		System.out.print(cnt1+" "+ cnt2);
		

	}
	
	public static int fib(int n) {
		if(n == 1 || n == 2) {
			cnt1++;
			return 1;
		}
		else return (fib(n-1) + fib(n-2));
	}
	
	public static int fibonacci(int n) {
		f[0] = 1;
		f[1] = 1;
		for(int i=2; i<n; i++) {
			f[i] = f[i-1]+ f[i-2];
			cnt2++;
		}
		return f[n-1];
	}

}
