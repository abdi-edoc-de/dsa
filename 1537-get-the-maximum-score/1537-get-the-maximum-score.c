long maxSum(int A[], int n, int B[], int m) {
    int i = 0, j = 0;
    long a = 0, b = 0, mod = 1000000007; // 1e9 + 7

    while (i < n || j < m) {
        if (i < n && (j == m || A[i] < B[j])) {
            a += A[i++];
        } else if (j < m && (i == n || A[i] > B[j])) {
            b += B[j++];
        } else {
            a = b = (a > b ? a : b) + A[i];
            i++, j++;
        }
    }

    return (a > b ? a : b) % mod;
}