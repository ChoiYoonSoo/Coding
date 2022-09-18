import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class BAEK1931 {

	public static void main(String[] args) {
		int room;
		int sTime = 0, cnt = 0;
		Scanner scan = new Scanner(System.in);
		room = scan.nextInt();
		
		int [][] Time = new int [room][2];
		
		for(int i=0; i<room; i++) {
			Time[i][0] = scan.nextInt();
			Time[i][1] = scan.nextInt();
		}
		
		Arrays.sort(Time,new Comparator<int[]>() {
			
			@Override
			public int compare(int[] t1, int[] t2) {
				if(t1[1] == t2[1]) {
					return t1[0] - t2[0];
					
				}
				return t1[1] - t2[1];
			}
		});
		
		for(int i=0; i<room; i++) {
			if(sTime <= Time[i][0]) {
				sTime = Time[i][1];
				cnt++;
			}
		}
		System.out.println(cnt);
		
	}

}
