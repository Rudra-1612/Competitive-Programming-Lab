def two_sum(nums: list[int], target: int) -> list[int]:
    """Return two distinct indices whose values add up to target."""
    seen = {}  # number -> index where it was first seen

    for index, number in enumerate(nums):
        complement = target - number

        if complement in seen:
            return [seen[complement], index]

        seen[number] = index

    return []  # No valid pair


if __name__ == "__main__":
    values = [2, 7, 11, 15]
    print("Indices:", two_sum(values, 9))
