import java.util.Scanner;

public class BAEK9461 {
	public static Long[] arr = new Long[101];

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		arr[0] = 0L;
		arr[1] = 1L;
		arr[2] = 1L;
		arr[3] = 1L;
		
		int T = in.nextInt();
		
		for(int i=0; i<T; i++) {
			int N = in.nextInt();
			System.out.println(pado(N));
		}
		
	}
	
	public static long pado(int N) {
		if(arr[N] == null) {
			arr[N] = pado(N-2) + pado(N-3);
		}
		return arr[N];
	}

}
