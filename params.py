# функция с праметрами по умолчанию:
def print_params(a=1, b='строка', c=3.5):
    print(a, b, c)



# print_params()
# print_params(a=4)
# print_params(b=False, c=6)
# print_params(b=25)
# print_params(c=[1, 2, 3])


# распаковка параметров:


value_list = [1, "Hello", 2.5]
value_dict = {'a': 1, 'b': 'строка', 'c': 4.5}
unpack1 = print_params(*value_list)
unpack2 = print_params(**value_dict)

#распковка + отдельные параметры

value_list2 = [5, 'Hi']
print_params(*value_list2)