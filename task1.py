import math
def calculate_sum():
    total_sum = 0.0
    for n in range(1, 51):
        chisl = math.cos(n)
        znam = (2 * n + 1) * (0.9 ** (2 * n + 1))
        term = ((-1) ** n) * (chisl / znam)
        total_sum += term
    return total_sum
result = calculate_sum()
print(f" {result:.3f}")