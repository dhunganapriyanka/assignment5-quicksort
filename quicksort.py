
import random
import time
import csv


# Partition the array around the selected pivot
def partition(arr, low, high, randomized=False):
    if randomized:
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Recursive Quicksort with reduced recursion depth
def quicksort_recursive(arr, low, high, randomized=False):
    while low < high:
        pivot = partition(arr, low, high, randomized)

        # Recursively sort the smaller partition first.
        # Continue with the larger partition in the loop.
        if pivot - low < high - pivot:
            quicksort_recursive(arr, low, pivot - 1, randomized)
            low = pivot + 1
        else:
            quicksort_recursive(arr, pivot + 1, high, randomized)
            high = pivot - 1


def deterministic_quicksort(arr):
    result = arr.copy()
    quicksort_recursive(result, 0, len(result) - 1)
    return result


def randomized_quicksort(arr):
    result = arr.copy()
    quicksort_recursive(result, 0, len(result) - 1, True)
    return result


def create_dataset(size, distribution):
    if distribution == "Random":
        return random.sample(range(size * 10), size)
    elif distribution == "Sorted":
        return list(range(size))
    elif distribution == "Reverse Sorted":
        return list(range(size, 0, -1))


def measure_time(algorithm, data):
    start = time.perf_counter()
    result = algorithm(data)
    elapsed = time.perf_counter() - start

    assert result == sorted(data), "Sorting failed!"
    return elapsed


def run_experiments():
    sizes = [500, 1000, 2000]
    distributions = ["Random", "Sorted", "Reverse Sorted"]
    algorithms = [
        ("Deterministic Quicksort", deterministic_quicksort),
        ("Randomized Quicksort", randomized_quicksort)
    ]

    results = []
    trials = 3

    print("\nQUICKSORT PERFORMANCE COMPARISON\n")

    for size in sizes:
        for distribution in distributions:
            data = create_dataset(size, distribution)

            for name, algorithm in algorithms:
                times = [
                    measure_time(algorithm, data)
                    for _ in range(trials)
                ]
                average = sum(times) / trials

                results.append([
                    name, size, distribution, f"{average:.6f}"
                ])

                print(
                    f"{name:25} | Size: {size:5} | "
                    f"{distribution:15} | "
                    f"Average: {average:.6f} seconds"
                )

    with open("results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Algorithm", "Input Size",
            "Distribution", "Average Time (seconds)"
        ])
        writer.writerows(results)

    print("\nResults saved to results.csv")


if __name__ == "__main__":
    example = [10, 7, 8, 9, 1, 5]

    print("Original:", example)
    print("Deterministic:", deterministic_quicksort(example))
    print("Randomized:", randomized_quicksort(example))

    run_experiments()
