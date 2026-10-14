n = int(input("\nВведите количество чисел: "))
nums = []
for i in range(n):
    nums.append(float(input(f"Введите число {i+1}: ")))
s = 0
cnt = 0
for i in range(1, n - 1):
    if nums[i - 1] < nums[i] < nums[i + 1]:
        s += nums[i]
        cnt += 1
print(f"Среднее арифметическое: {s / cnt}")