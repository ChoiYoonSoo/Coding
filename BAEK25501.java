import java.util.Scanner;

public class BAEK25501 {
	
	static int cnt = 0;
	
	public static int recursion(String s, int l, int r) {
		cnt++;
		if(l>=r) return 1;
		else if (s.charAt(l) != s.charAt(r)) return 0;
		else { 
			return recursion(s,l+1,r-1);
		}
	}
	
	public static int isPalindrome(String s) {
		return recursion(s,0,s.length()-1);
	}

	public static void main(String[] args) {
		int N;
		Scanner in = new Scanner(System.in);
		N = in.nextInt();

		for(int i=0; i<N; i++) {
			cnt = 0;
			System.out.println(isPalindrome(in.next())+" "+cnt);
		}
	}

}
