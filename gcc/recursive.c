#include <stdio.h>
double recursiveSum(double n) {
    if (n == 1) return 1;
    return n + recursiveSum(n-1);
}

double recursiveSum2(double n, double sum) {
    if (n == 1) return sum;
    return recursiveSum2(n-1, sum + n);
}

int main() {
    double sum1 = recursiveSum(100000);
    double sum2 = recursiveSum2(100000, 1);
    printf("%f, %f",sum1, sum2);

    return 1;
}
