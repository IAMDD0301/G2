def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print("從 1 加到 100 的總和：", sum_to_n(100))
total_50_to_100 = sum_to_n(100) - sum_to_n(49)
print("從 50 加到 100 的總和：", total_50_to_100)