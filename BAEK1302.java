import java.util.Arrays;
import java.util.Scanner;

public class BAEK1302 {

	public static void main(String[] args) {
		int N;
		int cnt = 0, max = 0, idx = 0;
		Scanner in = new Scanner(System.in);
		
		N = in.nextInt();
		String []book = new String[N];
		
		for(int i=0; i<N; i++) {
			book[i]=in.next();
		}
		
		Arrays.sort(book);
		String word = book[0];
		
		for(int i=1; i<N; i++) {
			if(book[i].equals(word)) {
				cnt++;
				if(max<cnt) {
					idx = i-1;
					max = cnt;
				}
			
			}
			else{
				word = book[i];
				cnt = 0;
			}
			
		}
		System.out.println(book[idx]);

	}

}
