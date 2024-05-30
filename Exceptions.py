def read_file(file_name):
    try:
        print("__CONTENT_START__")
        fp = open(file_name)
    except OSError:
        print("__NO_SUCH_FILE__")
    else:
        print("".join(fp.readlines()))
    finally:
        print("__CONTENT_END__")

# read_file("ABC\n")
# read_file("names.txt")


class UnderAge(Exception):
    def __init__(self, age):
        self._age = age

    def __str__(self):
        return f"Your age {self._age} is under 18 and in {18-self._age} years you could come to Ido birthday party"

    def get_age(self):
        return self._age


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as ua:
        print(ua)


send_invitation("Yonatan", 17)