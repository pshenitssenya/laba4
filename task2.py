import math
def calculate_product():
    total_product = 1.0
    for n in range(1, 11):
        chisl = n**2 + n + 1
        znam = (n / 10.0) ** (n / 10.0) + (n**2) / 2.0 + 9
        term = chisl / znam
        total_product *= term
    return total_product
result = calculate_product()
print(f"{result:.3f}")