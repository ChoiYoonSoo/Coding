// ���� �Ǻ���ġ �Լ�
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main(void) {
	int T, N, fib[41] = { 0,1 };
	scanf("%d", &T);
	for (int i = 2; i < 41; i++) {
		fib[i] = fib[i - 1] + fib[i - 2]; // �Ǻ���ġ �迭 ����
	}
	for (int i = 0; i < T; i++) {
		scanf("%d", &N);
		if (N == 0) printf("1 0\n");
		else printf("%d %d\n", fib[N - 1], fib[N]); // 0�� 1�� ����
	}

	return 0;
}