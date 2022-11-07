import java.util.Scanner;

public class BAEK1934 {

	public static void main(String[] args) {
		int N,A,B;
		Scanner in = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		N = in.nextInt();
		
		for(int i=0; i<N; i++) {
			A = in.nextInt();
			B = in.nextInt();
			int n = gdc(A,B);
			sb.append(A*B/n).append("\n");
		}
		
		System.out.println(sb);

	}
	public static int gdc(int a, int b) {
	    if(b==0)
	    	return a;
	    return gdc(b,a%b);
	}

}
