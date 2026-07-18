#include <stdio.h>
#include <math.h>

int main()
{
    int n;
    int a = 4, b = 2;

    printf("Enter transaction size (n): ");
    scanf("%d", &n);

    double logValue = log(a) / log(b);

    printf("\nMaster Theorem Analysis\n");
    printf("-----------------------\n");
    printf("Recurrence : T(n) = 4T(n/2) + n^2\n");
    printf("a = %d\n", a);
    printf("b = %d\n", b);
    printf("f(n) = n^2\n");
    printf("log_b(a) = %.0lf\n", logValue);

    if (logValue == 2)
    {
        printf("\nCase 2 of Master Theorem\n");
        printf("Time Complexity = Theta(n^2 log n)\n");
    }


    printf("\nAnalysis:\n");
    printf("The divide-and-conquer algorithm efficiently processes\n");
    printf("large banking transactions with complexity Theta(n^2 log n).\n");

    return 0;
}
