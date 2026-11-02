def single_number(nums: list[int]) -> int:
    """Find the value that occurs once when every other value occurs twice."""
    result = 0
    for number in nums:
        result ^= number
    return result


if __name__ == "__main__":
    values = [4, 1, 2, 1, 2]
    print("Single number:", single_number(values))
