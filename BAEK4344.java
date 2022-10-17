import java.util.Scanner;

public class BAEK4344 {

	public static void main(String[] args) {
		int N,M,num;
		int cnt=0;
		Scanner in = new Scanner(System.in);
		
		N = in.nextInt();
		double []arr = new double[N];
		
		for(int i=0; i<N; i++) {
			M = in.nextInt();
			double []a = new double[M];
			for(int j=0; j<M; j++) {
				num = in.nextInt();
				a[j] = num;
				arr[i] += num;
			}
			arr[i] = arr[i] / M;
			
			for(int z = 0; z<M; z++) {
				if(a[z] > arr[i]) {
					cnt++;
				}
			}
			arr[i] = (100.0/M) * cnt;
			cnt = 0;
			
		}
		for(int i=0; i<N; i++) {
			System.out.println(String.format("%.3f",arr[i])+"%");
		}

	}

}
