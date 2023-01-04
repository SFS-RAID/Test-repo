uin = input("Type the amount of money:")

with open('mydata.txt', 'w') as file:
  file.writelines(['Money = ' + uin + '\n', 'name = me'])
with open('mydata.txt', 'r') as file:
  contents = file.readlines()
  moneyline = contents[0].split(" ")
  money = moneyline[-1]
print(f"The amount of money is {money}")