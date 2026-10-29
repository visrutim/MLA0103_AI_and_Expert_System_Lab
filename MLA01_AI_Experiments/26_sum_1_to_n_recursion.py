"""Experiment 26: Sum of natural numbers from 1 to N using recursion."""

def sum_to_n(n):
    if n < 0:
        raise ValueError("N must be a non-negative integer.")
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)

if __name__ == "__main__":
    try:
        n = int(input("Enter a non-negative integer N: "))
        print(f"Sum of numbers from 1 to {n} =", sum_to_n(n))
    except (ValueError, RecursionError) as error:
        print("Please enter a reasonable non-negative integer.", error)
