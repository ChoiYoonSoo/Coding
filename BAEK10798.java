import java.util.Scanner;

public class BAEK10798 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		Character [][]str = new Character[5][15];
		
		for(int i=0; i<5; i++) {
			String st = in.next();
			int j=0;
			
			while(j < st.length()) {
				str[i][j] = st.charAt(j);
				j++;
			}
		}
		StringBuilder sb = new StringBuilder();
		
		for(int i=0; i<15; i++) {
			for(int j=0; j<5; j++) {
				if(str[j][i] != null) {
					sb.append(str[j][i]);
				}
			}
		}
		
		System.out.println(sb);

	}

}
