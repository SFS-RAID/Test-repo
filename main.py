uin = input("Type the amount of money:")
name = input("Type your name: ")

with open('mydata.txt', 'w') as file:
  file.writelines(['Money = ' + uin + '\n', 'name = ' + name])
with open('mydata.txt', 'r') as file:
  contents = file.readlines()
  moneyline = contents[0].split(" ")
  money = moneyline[-1]
  nameline = contents[1].split(" ")
  name = nameline[-1]
print(f"The amount of money is {money}")
print(f'Your name is {name}')
