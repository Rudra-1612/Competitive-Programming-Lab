def remove_duplicates(nums: list[int]) -> list[int]:
    """Remove repeats while preserving each value's first-occurrence order."""
    seen = set()
    result = []
    for number in nums:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result


if __name__ == "__main__":
    values = [4, 2, 4, 1, 2, 3, 1]
    print("Without duplicates:", remove_duplicates(values))
