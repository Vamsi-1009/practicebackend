#include <stdio.h>

int sum_v1(int num1, int num2);
int sum_v2(int num1, int num2);
int sum_v3(int num1, int num2);
int sum_v4(int num1, int num2);
int sum_v5(int num1, int num2);
void sum_v6(int num1, int num2);

int main()
{
    int num1 = 10;
    int num2 = 20;
    int result;
    result = sum_v1(num1, num2);
    printf("v1 main: %d\n\n", result);
    result = sum_v2(num1, num2);
    printf("v2 main: %d\n\n", result);
    result = sum_v3(num1, num2);
    printf("v3 main: %d\n\n", result);
    result = sum_v4(num1, num2);
    printf("v4 main: %d\n\n", result);
    result = sum_v5(num1, num2);
    printf("v5 main: %d\n\n", result);
    sum_v6(num1, num2);
    return 0;
}

int sum_v1(int num1, int num2)
{
    int sum;
    sum = num1 + num2;
    return sum;
}

int sum_v2(int num1, int num2)
{
    num1 = num1 + num2;
    return num1;
}

int sum_v3(int num1, int num2)
{
    return num1 + num2;
}

int sum_v4(int num1, int num2)
{
    int sum;
    sum = num1 + num2;
    printf("v4 function: %d\n", sum);
    return sum;
}

int sum_v5(int num1, int num2)
{
    num1 = num1 + num2;
    printf("v5 function: %d\n", num1);
    return num1;
}

void sum_v6(int num1, int num2)
{
    printf("v6 function: %d\n", num1 + num2);
}