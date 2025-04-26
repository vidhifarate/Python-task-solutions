import collections

def first_unique_char(s: str) -> str:
    char_counts = collections.Counter(s)
    for char in s:
        if char_counts[char] == 1:
            return char
    return "None"

s = "swiss"
result = first_unique_char(s)
print(f" {result}")