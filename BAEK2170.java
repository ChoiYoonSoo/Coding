import java.util.Scanner;

public class BAEK2170 {

	public static void main(String[] args) {
		int N;
		int x,y;
		int len = 0;
		Scanner in = new Scanner(System.in);
		
		N = in.nextInt();
		int [] arr = new int[2];
		
		x = in.nextInt();
		y = in.nextInt();
		arr[0] = x;
		arr[1] = y;
		len = y-x;
		
		for(int i=1; i<N; i++) {
			x = in.nextInt();
			y = in.nextInt();
			
			if(arr[1] > x) {
				if(arr[1] < y) {
					len += y - arr[1];
					arr[1] = y;
				}
			}
			else if(arr[1] < x) {
				len += y-x;
				arr[1] = y;
			}
			else if (arr[1] == x) {
				len += y-arr[1];
				arr[1] = y;
			}
		}
		System.out.println(len);

	}

}
