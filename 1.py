try:
    a = int(input())
    if a == 0:
     print('Wrong age')
    elif 1 < a < 18:
     print('Coca cola')
    elif 18 < a:
     print('Beer')
    else:
      print('error')
except ValueError:
    print("cannot divid by symbol")

a = int(input())
b = int(input())
summ = 0

for i in range(min(a, b), max(a, b) + 1):
 summ += i ** 2

print(summ)

list = [1, 2, "b"]
ind = int(input())

try:
    list[ind] = "hello"
except IndexError:
    print(f"Такого индекса нет, в списке всего {len(list)}элементов")

num_1 = float(input())
try:
    num_2 = float(input())
    act = input()

    if act == '+':
     print(num_1 + num_2)
    elif act == '*':
     print(num_1 * num_2)
    elif act == '/':
     print(num_1 / num_2)
    elif act == '-':
     print(num_1 - num_2)
    else:
     print('Такого знака нет')

except ValueError:
       print("Вы ввели не число")

num_1 = float(input())
num_2 = float(input())
act = input()

if act == '+':
    print(num_1 + num_2)
elif act == '*':
    print(num_1 * num_2)
elif act == '/':
    print(num_1 / num_2)
    

