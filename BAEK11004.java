import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BAEK11004 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int []arr = new int[N];
		
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		m_pivot_sort(arr,0,arr.length-1);
		
		System.out.println(arr[K-1]);
		
	}
	
	public static void m_pivot_sort(int[] arr, int lo, int hi) {
		if(lo>=hi) {
			return;
		}
		
		int pivot = partition(arr,lo,hi);
		
		m_pivot_sort(arr,lo,pivot);
		m_pivot_sort(arr,pivot+1,hi);
	}
	
	public static int partition(int []arr, int left, int right) {
		int lo = left -1;
		int hi = right +1;
		int pivot = arr[(left+right)/2];
		
		while(true) {
			
			do {
				lo++;
			}while(arr[lo] < pivot);
			
			do {
				hi--;
			}while(arr[hi] > pivot && lo <= hi);
			
			
			if(lo >= hi) {
				return hi;
			}
			
			swap(arr,lo,hi);
			
		}
	}
	
	public static void swap(int[] arr, int lo, int hi) {
		int temp = arr[lo];
		arr[lo] = arr[hi];
		arr[hi] = temp;
	}

}
