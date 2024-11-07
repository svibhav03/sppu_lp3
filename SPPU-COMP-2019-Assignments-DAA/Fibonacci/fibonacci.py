class Fibonacci:
    def __init__(self) -> None:
        pass

    def fib_solve(self, n):
        if n < 2:
            return n
        
        return  self.fib_solve(n-1) + self.fib_solve(n-2)
    
    def fibonacci_recursive(self, n):
        print("The fibonacci series by recursive algorithm is......")
        for i in range(0, n):
            print(self.fib_solve(i), end = " ")
        print()

    def fibonacci_iterative(self, n):
        print("The fibonacci series by iterative algorithm is......")

        f1 = 0
        f2 = 1
        print(f1, f2, end = " ")

        for _ in range(n-2):
            f3 = f1 + f2
            print(f3, end = " ")
            f1 = f2
            f2 = f3
        print()

f = Fibonacci()
f.fibonacci_recursive(10)
print()
f.fibonacci_iterative(10)


# def fibonacci_memoization(n, memo={}):
#     if n <= 1:
#         return n
#     if n not in memo:
#         memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
#     return memo[n]


# def fibonacci_optimized(n):
#     if n <= 1:
#         return n
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b


# def fibonacci_tabulation(n):
#     if n <= 1:
#         return n
#     fib = [0] * (n + 1)
#     fib[1] = 1
#     for i in range(2, n + 1):
#         fib[i] = fib[i - 1] + fib[i - 2]
#     return fib[n]

