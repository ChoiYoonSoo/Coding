import java.util.HashMap;
import java.util.Scanner;

public class BAEK1269 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int A = in.nextInt();
		int B = in.nextInt();
		
		HashMap<Integer,Integer> map1 = new HashMap<>();
		HashMap<Integer,Integer> map2 = new HashMap<>();
		
		for(int i=0; i<A; i++) {
			map1.put(i,in.nextInt());
		}
		
		for(int i=0; i<B; i++) {
			map2.put(in.nextInt(),i);
		}
		
		int cnt = 0;
		for(int i=0; i<A; i++) {
			if(map2.containsKey(map1.get(i))) {
				cnt+=2;
			}
		}
		
		System.out.println(A+B-cnt);
	}

}
