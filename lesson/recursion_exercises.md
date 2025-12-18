# Function Call Stack

## sum_of_two and max_of_two functions
Debug this code and see the call stack and return addresses.

```c
#include <stdio.h>

int max_of_two(int num1, int num2);
int sum_of_two(int num1, int num2);

int main()
{
    int num1, num2;
    int max, sum;
    num1 = 2;
    num2 = 3;
    
    max = max_of_two(num1, num2);
    sum = sum_of_two(num1, num2);
    printf("%d is greater.\n", max);
    printf("Sum of numbers is %d.\n", sum);
    return 0;
}

int max_of_two(int num1, int num2)
{
	int max;
	
    if (num2 > num1)
    {
    	max = num2;
    }
    else
    {
    	max = num1;
    }
    return max;
}

int sum_of_two(int num1, int num2)
{
    int sum;
    sum = num1 + num2;
    return sum;
}
```




# Recursion Exercises in C

## Instructions for Students

1. Do NOT compile and run the code until you have completed your prediction and trace
2. Write your trace showing each function call and what gets printed
3. Compare your prediction with actual output
4. If they differ, identify where your trace went wrong

---

## Part 1: Debugging Exercises

Debug the following programs by tracing through the recursive calls. Use print statements to understand the flow.

---

### Exercise 1A: Mutual Recursion

```c
#include <stdio.h>

int funcA(int n);
int funcB(int n);

int main() {
    int result1 = funcA(3);
    printf("Result 1: %d\n\n", result1);

    int result2 = funcA(4);
    printf("Result 2: %d\n", result2);

    return 0;
}

int funcA(int n) {
    printf("funcA called with n = %d\n", n);
    if (n <= 0) {
        return 1;
    }
    return n + funcB(n - 2);
}

int funcB(int n) {
    printf("funcB called with n = %d\n", n);
    if (n <= 0) {
        return 2;
    }
    return n * funcA(n - 1);
}
```

**Task:** Trace through both calls and explain why they produce different results.

---

### Exercise 1B: Single Recursion

```c
#include <stdio.h>

int mystery(int n);

int main() {
    int result1 = mystery(7);
    printf("Result 1: %d\n\n", result1);

    int result2 = mystery(483);
    printf("Result 2: %d\n", result2);

    return 0;
}

int mystery(int n) {
    printf("mystery called with n = %d\n", n);
    if (n < 10) {
        return n;
    }
    int lastDigit = n % 10;
    int remaining = n / 10;
    return lastDigit + mystery(remaining);
}

```

**Task:** Trace through both calls. What does this function compute?

---

## Part 2: Output Prediction Exercises

For each program below:
1. First, predict the output WITHOUT running the code
2. Then trace through the program step by step
3. Finally, run the code to verify your answer

---

### Sample 1: Mutual Recursion

```c
#include <stdio.h>

int ping(int n);
int pong(int n);

int main() {
    ping(5);
    printf("\n");
    return 0;
}

int ping(int n) {
    if (n <= 0) {
        return 0;
    }
    printf("%d ", n);
    return pong(n - 1);
}

int pong(int n) {
    if (n <= 0) {
        return 0;
    }
    printf("%d ", n * 2);
    return ping(n - 2);
}

```

**Your Predicted Output:**

```

```

---

### Sample 2: Tree Recursion

```c
#include <stdio.h>

int twist(int n);

int main() {
    int r = twist(4);
    printf("\nResult: %d\n", r);
    return 0;
}

int twist(int n) {
    if (n <= 0) {
        return 1;
    }
    printf("%d ", n);
    int result = twist(n - 3) + twist(n - 2);
    printf("%d ", n);
    return result;
}
```

**Your Predicted Output:**

```

```

---

### Sample 3: Mutual Recursion with Arithmetic

```c
#include <stdio.h>

int alpha(int n);
int beta(int n);

int main() {
    printf("A: %d\n", alpha(6));
    printf("B: %d\n", beta(5));
    return 0;
}

int alpha(int n) {
    if (n <= 1) {
        return 1;
    }
    return n + beta(n / 2);
}

int beta(int n) {
    if (n <= 1) {
        return 2;
    }
    return n * alpha(n - 1);
}

```

**Your Predicted Output:**

```

```

---

### Sample 4: Single Recursion with Expressions

```c
#include <stdio.h>

int scramble(int n);

int main() {
    int r = scramble(5);
    printf("\nResult: %d\n", r);
    return 0;
}

int scramble(int n) {
    if (n <= 0) {
        printf("%d ", 5 - n);
        return 2;
    }
    printf("%d ", n * 2 + 1);
    int result = scramble(n - 2);
    printf("%d ", result + n);
    return result + 1;
}

```

**Your Predicted Output:**

```

```

---

### Sample 5: Mutual Recursion with Expressions

```c
#include <stdio.h>

int up(int n);
int down(int n);

int main() {
    int r1 = up(3);
    printf("\nResult 1: %d\n\n", r1);
    
    int r2 = down(8);
    printf("\nResult 2: %d\n", r2);
    return 0;
}

int up(int n) {
    if (n >= 10) {
        printf("%d ", n % 7);
        return n;
    }
    printf("%d ", n + 3);
    return down(n + 4);
}

int down(int n) {
    if (n <= 2) {
        printf("%d ", n * 4);
        return n;
    }
    printf("%d ", 15 - n);
    return up(n - 1);
}
```

**Your Predicted Output:**

```

```
