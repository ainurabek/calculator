def add(n1, n2):
    return n1+n2
def multiple(n1,n2):
    return n1*n2
def subtract(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2

print("Выберите операцию:")
print("1.Сложение")
print("2.Вычитание")
print("3.Умножение")
print("4.Деление")

choice = input("Выберите вид операции(1/2/3/4):")

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
if num1/0:
    print ('Недопустимая операция')
else:
   print("Неверное значение")
