import java.util.Scanner;

public class BAEK1834 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long N = sc.nextInt();

		long sum = 0;
		
		for(long i = 1; i<= N-1; i++) {
			sum += (N*i) + i;
		}

		System.out.println(sum);

	}

}
