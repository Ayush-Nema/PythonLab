"""
This script demonstrates the general use of `deque` in Python.
"""

from collections import deque
from random import choice, randint
from timeit import timeit


class dequeBasics:
    """
    This class contains methods to demonstrate the basic operations of `deque`.
    """
    @staticmethod
    def deque_basics():
        """
        Deque is a double-ended queue. It can be used to add or remove elements from both ends.
        """
        fruits: deque[str] = deque(["apple", "orange", "banana"])
        fruits.append("tomato")
        fruits.appendleft("mango")
        print(fruits)

        print(f"Popped element: {fruits.pop()}, remaining deque: {fruits}")
        print(f"Popping element from left: {fruits.popleft()}, remaining deque: {fruits}")

        fruits.remove("orange")  # removing element without the knowledge of index
        print(f"Remaining deque after removal of one element: {fruits}")

        del fruits[0]
        print(fruits)

        fruits.pop()
        print(fruits)

    @staticmethod
    def maxlen_param():
        """
        The maxlen parameter is used to limit the number of elements in the deque.
        When the deque reaches the maximum length, the oldest element is automatically removed.
        """
        components = ["A", "B", "X"]
        belt: deque[str] = deque((), maxlen=5)

        for _ in range(50):
            belt.append(choice(components))
            print(belt)

    @staticmethod
    def rotate():
        """
        The `rotate` method rotates the deque n steps to the right if n is positive, to the left if n is negative.
        """
        fruits = deque(["mango", "apple", "orange", "banana"])
        print(f"Original deque: {fruits}")
        # print(fruits[2])

        # rotating the deque by 2 steps to the *right*
        fruits.rotate(-2)
        print(f"Right rotation: {fruits}")

        # rotating the deque by 2 steps to the *left*
        fruits.rotate(2)
        print(f"Left rotation: {fruits}")


class dequeBenchmarks:
    """
    This class contains methods to benchmark the performance of `deque` against `list`.
    """
    @staticmethod
    def benchmark_append():
        total_n = 1_000_000

        for i in range(0, (total_n // 10) + 1, total_n // 100):
            numbers = [randint(1, 100) for _ in range(total_n)]
            d_numbers = deque(numbers)

            t0 = timeit(
                "numbers.append(i)", globals={"numbers": numbers, "i": i}, number=total_n // 10
            )
            t1 = timeit(
                """numbers.append(i)""",
                globals={"numbers": d_numbers, "i": i},
                number=total_n // 10,
            )

            print(f"For index {i:,}:")
            print(f"  List: {t0:.5f} secs")
            print(f"  Deque: {t1:.5f} secs")
            print()

    @staticmethod
    def benchmark_insert():
        total_n = 500_000

        for i in range(0, total_n - 1000 + 1, total_n // 100):
            numbers = [randint(1, 100) for _ in range(total_n)]
            d_numbers = deque(numbers)

            t0 = timeit(
                "numbers.insert(i, i)", globals={"numbers": numbers, "i": i}, number=total_n // 100
            )
            t1 = timeit(
                """
numbers.rotate(-i)
numbers.appendleft(i)
numbers.rotate(i)
""",
                globals={"numbers": d_numbers, "i": i},
                number=total_n // 100,
            )

            print(f"For index {i:,}:")
            print(f"  List: {t0:.5f} secs")
            print(f"  Deque: {t1:.5f} secs")
            print()

    @staticmethod
    def benchmark_pop():
        total_n = 50000

        try:
            for i in range(0, total_n - 1000 + 1, total_n // 100):
                numbers = [randint(1, 100) for _ in range(total_n)]
                d_numbers = deque(numbers)

                t0 = timeit("numbers.pop(i)", globals={"numbers": numbers, "i": i}, number=total_n // 10)
                t1 = timeit(
                    """
numbers.rotate(-i)
numbers.popleft()
numbers.rotate(i)
""",
                    globals={"numbers": d_numbers, "i": i},
                    number=total_n // 10,
                )

                print(f"For index {i:,}:")
                print(f"  List: {t0:.5f} secs")
                print(f"  Deque: {t1:.5f} secs")
                print()

        except IndexError:
            print("Index limit reached, no further iters possible. Terminating.")


if __name__ == '__main__':
    # ======= Running the basic methods =======
    # dequeBasics.deque_basics()
    # dequeBasics.maxlen_param()
    # dequeBasics.rotate()

    # ======= Running the benchmarks =======
    # dequeBenchmarks.benchmark_append()
    # dequeBenchmarks.benchmark_insert()
    dequeBenchmarks.benchmark_pop()
