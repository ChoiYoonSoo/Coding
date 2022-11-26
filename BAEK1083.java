import java.util.Scanner;

public class BAEK1083 {

	public static void main(String[] args) {
		int n, s, i ,j;
		int []v = new int[50];
		Scanner in = new Scanner(System.in);
		n = in.nextInt();
		
		for(i=0; i<n; i++) {
			v[i]= in.nextInt();
		}
		s = in.nextInt();
		
		i=0;
		while(i<n) {
			int max=v[i], maxi = i;
			for(j=i+1; j<n && j<=i+s; j++) {
				if(max<v[j]) {
					max = v[j];
					maxi = j;
				}
				
			}
			s-=maxi-i;
			while(maxi>i) {
				v[maxi]=v[maxi-1];
				maxi--;
			
			}
			v[i]=max;
			i++;
		}
		for(i=0; i<n; i++) {
			System.out.print(v[i]+" ");
		}

	}

}
