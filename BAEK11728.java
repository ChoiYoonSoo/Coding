import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class BAEK11728 {

	public static void main(String[] args) throws IOException {
		int A,B;
		Scanner in = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		A = in.nextInt();
		B = in.nextInt();
		
		int [] arr1 = new int[A];
		int [] arr2 = new int[B];
		int [] arr3 = new int [A+B];
		
		for(int i=0; i<A; i++) {
			arr1[i] = in.nextInt();
			arr3[i] = arr1[i];
		}
		
		int idx = A;
		
		for(int i=0; i<B; i++) {
			arr2[i] = in.nextInt();
			arr3[idx++] = arr2[i];
		}
		
		Arrays.sort(arr3);
		
		for(int n:arr3) {
			sb.append(n).append(" ");
		}
		
		System.out.println(sb);
	}

}
