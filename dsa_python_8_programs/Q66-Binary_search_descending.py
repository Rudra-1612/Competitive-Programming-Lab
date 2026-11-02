def binary_search_descending(nums: list[int], target: int) -> int:
    """Return target's index in a descending sorted list, or -1 if absent."""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # In descending order, larger values are to the left.
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == "__main__":
    values = [90, 75, 60, 45, 30, 15]
    print("Index of 60:", binary_search_descending(values, 60))
    print("Index of 50:", binary_search_descending(values, 50))
