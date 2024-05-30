from functools import reduce


def combine_coins(coin, numbers):
    return ", ".join([coin + str(num) for num in numbers])


# print(combine_coins('$', range(5)))


def dup_each_char(letter):
    return letter + letter


def double_letter(my_str):
    return ''.join(map(dup_each_char, my_str))

# print(double_letter("python"))
# print(double_letter("we are the champions!"))


def is_divide_by_4(number):
    return int(number) % 4 == 0


def four_dividers(number):
    return list(filter(is_divide_by_4, range(1, number + 1)))


# print(four_dividers(9))
# print(four_dividers(3))

def add(a, b):
    return int(a) + int(b)


def sum_of_digits(number):
    return reduce(add, str(number))

# print(sum_of_digits(10492))


# def function(num, item):
#     return num + 1
# password = input("Enter Your password (integers only): ")
# lst = list(map(int, password))
# magic = reduce(function, lst)
# result = (lambda x: x % 4 == 0)(magic)
# if result:
#     print("Correct password!")
# else:
#     print("Wrong password.")


def intersection(list_1, list_2):
    return list(set([x for x in list_1 if x in list_2]))


# print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))


def is_prime(number):
    return bool(len([x for x in range(2, number) if number % x == 0]))


# print(is_prime(43))


def is_funny(string):
    return not bool(len([char for char in string if char not in 'ha']))


# print(is_funny("hahahahahaha"))


password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
password = "".join([chr(ord(char) + 2) if char.isalpha() else char for char in password])
# print(password)

