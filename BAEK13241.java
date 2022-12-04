import java.util.Scanner;

public class BAEK13241 {

	public static void main(String[] args) {
		long A,B;
		Scanner in = new Scanner(System.in);
		
		A = in.nextLong();
		B = in.nextLong();
		
		System.out.println(A*B/gcd(A,B));

	}
	
	public static long gcd(long a, long b) {
		if(b==0) return a;
		
		else return gcd(b,a%b);
	}

}
