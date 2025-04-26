

def find_missing_number(arr: list) -> int:
    n = len(arr)
    xor_sum = 0
    for i in range(n + 1):
        xor_sum ^= i
    for num in arr:
        xor_sum ^= num
    return xor_sum

arr = [3, 0, 1]
result = find_missing_number(arr)
print(f" {result}")