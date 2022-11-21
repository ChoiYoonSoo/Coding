import java.util.Scanner;

public class BAEK1748 {

	public static void main(String[] args) {
		int N;
		int len = 0;
		Scanner in = new Scanner(System.in);
		
		N = in.nextInt();
		
		for(int i=1; i<=N; i++) {
			if(i<10) {
				len+=1;
			}
			else if(i<100) {
				len+=2;
			}
			else if(i<1000) {
				len+=3;
			}
			else if(i<10000) {
				len+=4;
			}
			else if(i<100000) {
				len+=5;
			}
			else if(i<1000000) {
				len+=6;
			}
			else if(i<10000000) {
				len+=7;
			}
			else if(i<100000000) {
				len+=8;
			}
			else if(i<1000000000) {
				len+=9;
			}
		}
		System.out.println(len);
	}

}
