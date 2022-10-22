import java.util.Scanner;
import java.util.Stack;

public class BAEK10773 {

	public static void main(String[] args) {
		int n,m,sum=0;
		Stack<Integer> stack = new Stack<Integer>();
		Scanner in = new Scanner(System.in);
		
		n = in.nextInt();
		
		for(int i=0; i<n; i++) {
			m=in.nextInt();
			if(m != 0) {
				stack.push(m);
			}
			else if(m == 0 && !stack.isEmpty()) {
				stack.pop();
			}
		}
		
		while(!stack.isEmpty()) {
			sum += stack.pop();
		}
		
		System.out.println(sum);
	}

}
