#1) необходимо разработать функцию, принимающую список строк и строку, и
#выполняющую вставку строки в середину списка (если длина списка 
#нечетная, то вставлять строку перед серединным элементом);
#2
s = input("Введите строку: ")
index = int(input("Введите позицию: "))
b = input("Введите строку: ")
def insert_dash(s, index):
    if index > len(s):
        return print("paste operation is not possible")
    return s[:index] + b + s[index:]
print(insert_dash(s, index)) 
#3) необходимо разработать функцию, принимающую список строк и число, и 
#выполняющую удаление строки по указанной позицию списка, если удаление
#невозможно, то вернуть сообщение «delete operation is not possible».
