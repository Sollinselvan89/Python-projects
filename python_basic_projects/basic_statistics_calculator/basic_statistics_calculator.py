"""
A simple statistics calculator that accepts a list of numbers and
computes mean, median, mode, minimum, maximum, and range with input
validation and clean output.
"""

def get_user_input() -> list[float]:
    """
    Prompt the user for a comma-separated list of numbers.
    Validate each entry and return a clean list of floats.
    """
    while True:
        number_str_list = input(
            "Please enter a list of numbers (2 decimals) separated by commas: "
        )

        split_num_list = number_str_list.split(",")
        num_list: list[float] = []
        invalid = False

        for num_str in split_num_list:
            num_str = num_str.strip()  # correction: trim whitespace

            if num_str == "":
                # skip empty entries like ",,"
                continue

            try:
                num = float(num_str)
            except ValueError:
                print("Only numbers please.")
                invalid = True
                break

            num_list.append(num)

        if invalid:
            continue  # correction: reprompt on invalid input

        return num_list


def calculate_mean(numbers: list[float]) -> tuple[float, int]:
    """
    Return the mean (average) of the list and the count of numbers.
    """
    count = len(numbers)
    total = 0.0

    for num in numbers:
        total += num

    return total / count, count


def calculate_median(numbers: list[float]) -> float:
    """
    Return the median value from a list of numbers.
    The list is sorted in place.
    """
    numbers.sort()  # correction: do not assign sort() result

    length = len(numbers)
    mid = length // 2

    if length % 2 == 0:
        # correction: use / not // to avoid losing decimals
        median = (numbers[mid - 1] + numbers[mid]) / 2
    else:
        median = numbers[mid]

    return median


def find_mode(numbers: list[float]) -> list[float] | str:
    """
    Return the mode(s) of the numbers.
    If all values appear only once, return 'no mode'.
    """
    mode_dict: dict[float, int] = {}

    # Count occurrences
    for num in numbers:
        if num in mode_dict:
            mode_dict[num] += 1  # correction: simpler increment
        else:
            mode_dict[num] = 1

    # Find maximum frequency
    max_count = 1
    for value in mode_dict.values():
        if value > max_count:
            max_count = value

    if max_count == 1:
        return "no mode"

    # Collect all numbers with max_count
    mode_list: list[float] = []
    for key, value in mode_dict.items():
        if value == max_count:
            mode_list.append(key)

    return mode_list


def calculate_max(numbers: list[float]) -> float:
    """
    Find the maximum number without using built-in max().
    """
    max_value = numbers[0]  # correction: do not rely on sorted order

    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value


def calculate_min(numbers: list[float]) -> float:
    """
    Find the minimum number without using built-in min().
    """
    min_value = numbers[0]  # correction: do not rely on sorted order

    for num in numbers:
        if num < min_value:
            min_value = num

    return min_value


def calculate_range(max_value: float, min_value: float) -> float:
    """
    Return the range (max - min).
    """
    return max_value - min_value


def main() -> None:
    """
    Collect user input and print all basic statistics.
    """
    num_list = get_user_input()

    mean, count = calculate_mean(num_list)
    median = calculate_median(num_list)
    mode = find_mode(num_list)
    min_value = calculate_min(num_list)
    max_value = calculate_max(num_list)
    range_value = calculate_range(max_value, min_value)

    print("\nHere are the basic statistics of your numbers:\n")
    print(f"Numbers entered: {num_list}")
    print(f"Count: {count}")
    print(f"Mean / Average: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Minimum: {min_value}")
    print(f"Maximum: {max_value}")
    print(f"Range: {range_value}")


if __name__ == "__main__":
    main()

