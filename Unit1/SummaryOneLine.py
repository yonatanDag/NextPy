from functools import reduce

# question 1
with open("names.txt", 'r') as file_object:
    print(reduce(lambda word1, word2: word1 if len(word1) > len(word2) else word2, [word.strip() for word in file_object.readlines()]))


# question 2
with open("names.txt", 'r') as file_object:
    print(reduce(lambda a, b: a + b, [len(word.strip()) for word in file_object.readlines()]))


# question 3
with open("names.txt", 'r') as file_object:
    words = sorted([word.strip() for word in file_object.readlines()], key=len)
    print("\n".join(word for word in words if len(word) == len(words[0])))


# question 4
with open("names.txt", 'r') as file_object:
    words_length = [len(word.strip()) for word in file_object.readlines()]
    print("\n".join(str(length) for length in words_length))


# question 5
with open("names.txt", 'r') as file_object:
    length = int(input("Enter name Length: "))
    print("\n".join([word.strip() for word in file_object.readlines() if len(word.strip()) == length]))