#include <stdio.h>
#include <math.h>

int main()
{
    int n;
    int a = 2, b = 2;

    printf("Enter audio input size (n): ");
    scanf("%d", &n);

    double logValue = log(a) / log(b);

    printf("\nMaster Theorem Analysis\n");
    printf("-----------------------\n");
    printf("Recurrence : T(n) = 2T(n/2) + sqrt(n)\n");
    printf("a = %d\n", a);
    printf("b = %d\n", b);
    printf("f(n) = sqrt(n)\n");
    printf("log_b(a) = %.0lf\n", logValue);

    printf("\nCase 1 of Master Theorem\n");
    printf("Time Complexity = Theta(n)\n");

    printf("\nAnalysis:\n");
    printf("The speech recognition system processes\n");
    printf("large audio inputs with linear time complexity.\n");

    return 0;
}
