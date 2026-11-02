def xor_swap(a: int, b: int) -> tuple[int, int]:
    """Return (b, a) using XOR, without a temporary variable."""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


if __name__ == "__main__":
    x, y = 10, 20
    print("Before:", x, y)
    x, y = xor_swap(x, y)
    print("After: ", x, y)
