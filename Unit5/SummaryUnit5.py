def check_id_valid(id_number):
    """
    checks if the ID number is valid according to the requirements.
    param id_number: the ID number to check
    type id_number: int
    return: True if the ID number is valid, False otherwise
    type: bool
    """
    copy_id = id_number
    sum_numbers = 0

    while copy_id > 9:
        # add the last digit to the sum
        sum_numbers += copy_id % 10
        copy_id = copy_id // 10
        even_digit = 2 * (copy_id % 10)
        # if the result is greater than 9, sum the digits of the result
        if even_digit > 9:
            even_digit = (even_digit % 10) + int(even_digit / 10)
        sum_numbers += even_digit
        copy_id = copy_id // 10
    sum_numbers += copy_id

    # check if the total sum is divisible by 10
    return sum_numbers % 10 == 0


# print(check_id_valid(123456780))
# print(check_id_valid(123456782))


class IDIterator:
    """
    An iterator class to generate valid ID numbers starting from a given ID.
    """
    def __init__(self, id_):
        """
        Initializes the IDIterator with a starting ID.
        param id_: The starting ID number
        type id_: int
        """
        self._id = id_

    def __iter__(self):
        """
        returns the iterator object itself.
        return: The iterator object
        type: IDIterator
        """
        return self

    def __next__(self):
        """
        returns the next valid ID number in the sequence.
        return: The next valid ID number
        type: int
        raise: StopIteration if the ID number bigger than 999999999
        """
        self._id += 1
        while self._id <= 999999999:
            if check_id_valid(self._id):
                current_id = self._id
                self._id += 1
                return current_id
            self._id += 1
        raise StopIteration


def id_generator(input_id):
    """
    generator function to yield valid ID numbers starting from a given ID.
    param input_id: The starting ID number
    type input_id: int
    yield: The next valid ID number
    type: int
    """
    id_ = input_id + 1
    while id_ <= 999999999:
        if check_id_valid(id_):
            yield id_
        id_ += 1


def main():
    """
    main function to prompt the user for an ID number and generate the next 10 valid IDs.
    """
    input_id = int(input("Enter ID: "))
    gen_or_it = input("Generator or Iterator? (gen/it)? ")

    if gen_or_it == "it":
        iterator = IDIterator(input_id)
        for _ in range(10):
            print(next(iterator))
    elif gen_or_it == "gen":
        gen = id_generator(input_id)
        for _ in range(10):
            print(next(gen))


if __name__ == "__main__":
    main()
