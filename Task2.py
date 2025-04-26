def is_valid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack

s1 = "{[()]}"
s2 = "{[(])}"

print(f"'{s1}' is valid: {is_valid(s1)}")
print(f"'{s2}' is valid: {is_valid(s2)}")