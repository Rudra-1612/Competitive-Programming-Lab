def is_valid_parentheses(text: str) -> bool:
    """Check whether (), {}, [] are correctly matched and nested."""
    opening_for = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in text:
        if char in "({[":
            stack.append(char)
        elif char in opening_for:
            if not stack or stack.pop() != opening_for[char]:
                return False
        else:
            # The assignment specifies bracket-only input.
            return False

    return len(stack) == 0


if __name__ == "__main__":
    print("([]{}) ->", is_valid_parentheses("([]{})"))
    print("([)]   ->", is_valid_parentheses("([)]"))
