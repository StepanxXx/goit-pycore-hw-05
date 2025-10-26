"""
Memoized Fibonacci factory.
"""

from typing import Callable, Dict


def caching_fibonacci() -> Callable[[int], int]:
    """
    Return a memoized Fibonacci function.
    """
    cache: Dict[int, int] = {}

    def fibonacci(n: int) -> int:
        """
        Compute Fibonacci number for n using recursion with memoization.
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

if __name__ == "__main__" :
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()

    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610
