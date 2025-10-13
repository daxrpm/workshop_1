from typing import List


# First algorithm


def sum_convergence_with_error(max_error: float) -> None:
    """Sum convergence until a given error

    Args:
        max_error (float): tolerated error
    """

    sum: float = 1
    counter: int = 0
    divider: int = 2
    while (True):

        sum = sum + 1/divider

        divider *= 2
        print(sum)
        counter += 1
        if ((2-sum) <= max_error):
            print(counter)
            break


# Second algorithm


def bubble_sort(vector: List[float]) -> List[float]:
    """Sort a vector of numbers

    Args:
        vector (List[float]): Vector to be sorted

    Returns:
        List[float]: Sorted Vector
    """
    for i in range(0, len(vector)):
        swapped: bool = False
        for j in range(1, len(vector)-i):
            if (vector[j] < vector[j - 1]):
                vector[j], vector[j - 1] = vector[j - 1], vector[j]
                swapped = True
        if (not swapped):
            break
    return vector


# Third Algorithm

def fibonacci(n: int) -> int:
    if (n == 0):
        return 0
    else:
        x: int = 0
        y: int = 1
        for i in range(1, n):
            z: int = x + y
            x = y
            y = z
    return y


def main():
    sum_convergence_with_error(0.1)

    vector: List[float] = [5, 8, 9, 1, 4, 5, 3]

    print(bubble_sort(vector))

    print(fibonacci(11))


if __name__ == "__main__":
    main()
