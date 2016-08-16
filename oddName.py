"""
Receives a name as input and the number of letters skipped before
"""
__author__ = 'Gareth'


def main():
    name = get_name()
    num_of_letters = int(input("Number of letters skipped. ")) + 1
    print_name(name, num_of_letters)


def print_name(name, num_of_letters):
    temp = 0
    if num_of_letters == 1:
        for i in name:
            print(i, end=" ")
    else:
        for i in name:
            temp += 1
            if temp % num_of_letters == 1:
                print(i, end=" ")


def get_name():
    name = input("Please enter your name. ")
    while any(i.isdigit() for i in name):
        name = input("The name entered contained a number, please renter your name. ")
    return name


if __name__ == "__main__":
        main()