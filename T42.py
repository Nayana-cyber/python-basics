#Python Program to Print the Fibonacci sequence?

def print_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
num_terms = int(input("Enter the number of terms: "))
print_fibonacci(num_terms)


