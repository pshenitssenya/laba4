n = int(input())
nums = []
for i in range(n):
    nums.append(float(input(f"Введите число {i+1}: ")))
odd_sum = odd_cnt = 0 
even_sum = even_cnt = 0  
for i, x in enumerate(nums):
    number = i + 1
    if number % 2 == 1:
        odd_sum += x
        odd_cnt += 1
    else:
        even_sum += x
        even_cnt += 1
avg_odd = odd_sum / odd_cnt if odd_cnt else 0
avg_even = even_sum / even_cnt if even_cnt else 0
print(f"Среднее арифметическое нечётных номеров: {avg_odd}")
print(f"Среднее арифметическое чётных номеров: {avg_even}")
print(f"Частное: {avg_odd / avg_even}")