from typing import List, Dict
import seaborn as sns
import matplotlib.pyplot as plt
from random import randint

# First algorithm


def sum_convergence_with_error(max_error: float) -> None:
    """Sum convergence until a given error

    Args:
        max_error (float): tolerated error
    """

    sum: float = 1
    counter: int = 1  # 1 thinking that the 1 counts as an add
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
    counter: int = 0
    for i in range(0, len(vector)):
        swapped: bool = False
        for j in range(1, len(vector)-i):
            if (vector[j] < vector[j - 1]):
                vector[j], vector[j - 1] = vector[j - 1], vector[j]
                counter += 1
                swapped = True
        if (not swapped):
            break
    print(f"{counter} swaps were done")
    return vector


# Third Algorithm

def fibonacci(n: int) -> int:
    """Fibonacci sequence

    Args:
        n (int): non negative integer

    Returns:
        int: fibonacci value at n iterations
    """
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


def fill_with_fibonacci_data(iterations: int) -> Dict[str, List[float]]:
    """Fill a dictionary with fibonacci values

    Args:
        iterations (int): number of iterations for fibonacci values

    Returns:
        Dict[str, List[float]]: dictionary with x and y values for plotting
    """
    x_values: List[float] = [float(i) for i in range(0, iterations)]
    values: Dict[str, List[float]] = {"x": x_values}
    values["y"] = [fibonacci(int(i)) for i in x_values]
    return values


def plot_fibonacci_values(iterations: int) -> None:
    """Plots fibonacci values with n iterations

    Args:
        iterations (int): number of iterations
    """
    fibonacci_data: Dict[str, List[float]
                         ] = fill_with_fibonacci_data(iterations)

    sns.set_theme()
    sns.lineplot(x=fibonacci_data["x"], y=fibonacci_data["y"])
    plt.title("Fibonacci Values")
    plt.xlabel("n value")
    plt.ylabel("Fibonacci value")
    plt.show()


def plot_fibonacci_div(iterations: int) -> None:
    """Plots fibonacci values division with the previous value in n iterations

    Args:
        iterations (int): number of iterations
    """

    fibonacci_data: Dict[str, List[float]
                         ] = fill_with_fibonacci_data(iterations)
    sns.relplot(x=fibonacci_data["x"][2:], y=[
                fibonacci_data["y"][i]/fibonacci_data["y"][i-1] for i in range(2, len(fibonacci_data["y"]))], kind="line")
    plt.title("Fibonacci Div")
    plt.xlabel("n value")
    plt.ylabel("Fibonacci value / fib value -1")
    plt.show()


def main():

    # First Algorithm """
    sum_convergence_with_error(0.1)

    # Second Algorithm
    worst_case: List[float] = [5, 4, 3, 2, 1]
    best_case: List[float] = [1, 2, 3, 4, 5]

    vector2: List[float] = [float(randint(-200, 145))
                            for i in range(0, 100000)]
    print("In the worst case: ", bubble_sort(worst_case))
    print("In the best case: ", bubble_sort(best_case))
    # print(bubble_sort(vector2))

    # Third Algorithm
    plot_fibonacci_values(8)
    plot_fibonacci_div(700)


if __name__ == "__main__":
    main()
