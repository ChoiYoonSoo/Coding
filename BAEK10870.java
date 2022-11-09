import java.util.Scanner;

public class BAEK10870 {

	public static void main(String[] args) {
		int N;
		Scanner in = new Scanner(System.in);
		
		N = in.nextInt();
		System.out.println(fib(N));

	}
	
	public static int fib(int n) {
		if(n==0) return 0;
		else if(n==1) return 1;
		
		else return fib(n-1) + fib(n-2);
	}

}
