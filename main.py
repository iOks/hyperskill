print('Prices:')
print('Bubblegum: $2')
print('Toffee: $0.2')
print('Ice cream: $5')
print('Milk chocolate: $4')
print('Doughnut: $2.5')
print('Pancake: $3.2')
print("")
print('Earned amount:')
print('Bubblegum: $202')
print('Toffee: $118')
print('Ice cream: $2250')
print('Milk chocolate: $1680')
print('Doughnut: $1075')
print('Pancake: $80')
print("")
bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80
income = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake
print(f"Income: $", income)

print('Staff expenses:')
staff_expenses = int(input())
print('Other expenses:')
other_expenses = int(input())
net_income = income - staff_expenses - other_expenses
print(f'Net income: $', net_income)
