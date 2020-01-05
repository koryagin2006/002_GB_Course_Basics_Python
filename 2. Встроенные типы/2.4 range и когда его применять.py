# range
numbers = range(10)
print(numbers)  # <class 'range'> диапазон
print(list(numbers))

# вывести нечетные числа от 1 до n
n = 100
print(list(range(1, n, 2)))

# Когда нам нужен range
winners = ['Max', 'Leo', 'Kate']

# простой перебор
for winner in winners:
    print(winner)

# используем range
for i in range(len(winners)):
    # print(i+1)
    print(i + 1, ')', winners[i])
