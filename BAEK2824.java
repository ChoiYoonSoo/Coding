import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class BAEK2824 {

	public static void main(String[] args) throws IOException {
		int N, M;
		BigInteger a = new BigInteger("1");
		BigInteger b = new BigInteger("1");
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		
		for(int i=0; i<N; i++) {
			a = a.multiply(new BigInteger(st.nextToken()));
		}
		
		M = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		
		for(int i=0; i<M; i++) {
			b = b.multiply(new BigInteger(st.nextToken()));
		}
		
		String temp = a.gcd(b).toString();
		
		if(temp.length() > 9)
			System.out.println(temp.substring(temp.length()-9,temp.length()));
		else
			System.out.println(temp);
		
	}
	
	public static long cal(long r, long b) {
		if(b==0) return r;
		
		return cal(b,r%b);
	}

}
