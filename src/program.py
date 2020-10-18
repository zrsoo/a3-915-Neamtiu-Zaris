#
# Write the implementation for A3 in this file
#

# Font customization


yellow = '\u001b[33m'  # Yellow text
endc = '\033[m'  # Reset to default text
blue = '\u001b[34m'  # Blue text
green = '\u001b[32m'  # Green text
red = '\u001b[31m'  # Red text
bold = '\u001b[1m'  # Bold text
underlined = '\u001b[4m'  # Underlined text


#
# domain section is here (domain = numbers, transactions, expenses, etc.)
# getters / setters
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)


def get_realp(nr):
    return nr[0]


def get_imaginaryp(nr):
    return nr[1]


def set_realp(nr, realp):
    nr[0] = int(realp)


def set_imaginaryp(nr, imaginaryp):
    nr[1] = int(imaginaryp)


# Functionalities section (functions that implement required features)
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)
# Each function does one thing only
# Functions communicate using input parameters and their return values


def create_complex(str_complex):
    """
    Transforms the string "a + bi" into a storage-friendly object
    :param str_complex: "a + bi", where a and b are integers
    :return: A list containing the real and imaginary part of the complex number
    """

    if len(str_complex) < 4:
        raise ValueError

    # Removing the "i".
    str_complex = str_complex.strip("i")

    # If there is a minus on the first position, then the real part is negative
    if str_complex[0] == '-':
        realp_negative = 1
    else:
        realp_negative = 0

    # If there is a minus beyond position 1, then we know
    # for sure that the imaginary part is negative, we
    # need this in order to know if we are going to use "+"
    # or "-" when splitting.
    if '-' in str_complex[1:]:
        imagp_negative = 1
    else:
        imagp_negative = 0

    if imagp_negative == 1:
        nr = str_complex.split("-")
    else:
        nr = str_complex.split("+")

    nr_complex = [''] * 2

    if realp_negative and imagp_negative:
        nr.remove('')
        set_realp(nr_complex, -int(nr[0]))
    else:
        set_realp(nr_complex, nr[0])

    if imagp_negative == 1:
        set_imaginaryp(nr_complex, -int(nr[1]))  # If the imaginary part is negative, we set it as such.
    else:
        set_imaginaryp(nr_complex, nr[1])

    return nr_complex


def format_input(input_str):
    """
    Using the input string, builds a list containing the user command
    and the arguments of the command
    :param input_str: The string that the user typed
    :return: A list containing the command and its arguments
    """

    cmd_list = input_str.split()
    return cmd_list


def add_complex(li_complex, nr):
    li_complex.append(nr)


# UI section
# (all functions that have input or print statements, or that CALL functions with print / input are  here).
# Ideally, this section should not contain any calculations relevant to program functionalities


def print_menu():
    """Prints the user menu"""

    print(bold + underlined + "\nList of commands:", endc + "\n")
    print(green + "add \"a+bi\"" + endc + " - adds the complex number to the list")
    print(
        green + "insert \"a+bi\" at \"x\"" + endc + " - inserts the complex number at position x (positions are numbered"
                                                    " starting from 0)\n")
    print(red + "remove \"x\"" + endc + " - removes the number at position x from the list")
    print(red + "remove \"x\" to \"y\"" + endc + " - removes the numbers from position x to position y"
                                                 " (including the numbers situated on position x and y)\n")
    print(blue + "replace \"a+bi\" with \"c+di\"" + endc + " - replaces all occurrences of a+bi with c+di\n")
    print(yellow + "list " + endc + "- displays the list of numbers")
    print(yellow + "list real \"x\" to \"y\"" + endc + " - display the real numbers (imaginary part = 0) beginning "
                                                       "at index x and ending at index y")
    print(
        yellow + "list modulo \"symbol\" \"x\"" + endc + " - (where symbol ∈ [ < , = , > ]) display all numbers having "
                                                         "modulo in a certain way (example: list modulo < 10, list modulo = 5)\n")
    print(red + bold + "exit" + endc)


def print_complex(nr):
    """Prints a complex number a user-friendly way"""
    realp = get_realp(nr)
    imaginaryp = get_imaginaryp(nr)

    imaginaryp_negative = 0

    if realp == 0:
        print(str(imaginaryp) + 'i')
        return

    if imaginaryp < 0:
        imaginaryp = -imaginaryp
        imaginaryp_negative = 1

    if imaginaryp == 0:
        print(realp)
        return

    elif imaginaryp_negative == 0:
        print(str(realp) + " + " + str(imaginaryp) + 'i')
    else:
        print(str(realp) + " - " + str(imaginaryp) + 'i')


def print_list(li_complex):
    for index in range(0, len(li_complex)):
        print(str(index + 1) + ".)", end=" ")
        print_complex(li_complex[index])


def start():
    """Control function"""

    print_menu()  # Printing the user menu

    # Testing
    li_complex = []
    test_init(li_complex)
    #

    cmds = ["add", "insert", "remove", "replace", "list", "exit"]

    while (1):
        # Getting user input and formatting it

        input_str = input("\nWhat would you like to do?\n")
        input_list = format_input(input_str)

        #

        # Calling functions for desired command

        command = input_list[0]

        if command not in cmds or len(input_list) > 5:
            print("The command you have typed does not belong to the list of "
                  "implemented commands.")

        elif command == "add":

            try:
                nr = create_complex(input_list[1])
                add_complex(li_complex, nr)

                print("You have successfully added a complex number to the list.")
            except:
                print("The complex number you have typed is of incorrect form!")

        elif command == "insert":

            try:
                nr = create_complex(input_list[1])
                index = int(input_list[3])

                if input_list[2] != "at":
                    raise ValueError

                if index < 0 or index > len(li_complex) + 1:
                    raise IndexError

                li_complex.insert(index - 1, nr)

                print("You have successfully inserted your complex number at position " + str(index) + ".")
            except ValueError:
                print("The command you have entered is not of correct form!")
            except IndexError:
                print("The index you have typed is out of range!")

        elif command == "remove":
            try:
                nr_cmds = len(input_list)

                if nr_cmds == 2:

                    index = int(input_list[1])
                    li_complex.pop(index - 1)

                    print("You have successfully removed the complex number at position " + str(index))

                elif nr_cmds == 4:

                    sindex = int(input_list[1])
                    eindex = int(input_list[3])
                    nrpops = eindex - sindex + 1

                    for index in range(0, nrpops):
                        li_complex.pop(sindex - 1)

                    print("You have successfully removed the complex numbers from "
                          "position " + str(sindex) + " to position " + str(eindex))
            except ValueError:
                print("You did not type an index!")
            except IndexError:
                print("The index you have typed is out of range")

        elif command == "replace":

            try:
                complex_tbr = create_complex(input_list[1])
                complex_rpm = create_complex(input_list[3])

                if complex_tbr not in li_complex:
                    raise IndexError

                li_complex = [element if element != complex_tbr else complex_rpm for element in li_complex]

                print("You have successfully performed the operation!")
            except ValueError:
                print("The complex numbers you have typed are of incorrect form!")
            except IndexError:
                print("The complex number you want to replace does not exist in the list!")

        elif command == "list":

            nr_cmds = len(input_list)

            if nr_cmds == 1:
                print(yellow + "\nThe list of complex numbers is: " + endc)
                print_list(li_complex)

            elif nr_cmds == 5:
                try:
                    if input_list[1] != "real" or input_list[3] != "to":
                        raise ValueError

                    spos = int(input_list[2]) - 1
                    epos = int(input_list[4]) - 1

                    if spos < 0 or epos > len(li_complex):
                        raise IndexError

                    for index in range(spos, epos + 1):
                        if get_imaginaryp(li_complex[index]) == 0:
                            print_complex(li_complex[index])
                except ValueError:
                    print("The command you have entered is not of correct form!")
                except IndexError:
                    print("The indexes you have typed are out of range!")


        elif command == "exit":
            return

    #


# Test functions go here
#
# Test functions:
#   - no print / input
#   - great friends with assert

def test_init(li_complex):
    # use this function to add the 10 required items
    # use it to set up test data

    li_append(li_complex)

    # Add function
    add_complex(li_complex, [2, -7])
    assert len(li_complex) == 10
    #

    #


def li_append(li_complex):
    li_complex.append([2, 3])
    li_complex.append([-1, 2])
    li_complex.append([0, -10])
    li_complex.append([-15, 20])
    li_complex.append([120, -156])
    li_complex.append([10, 0])
    li_complex.append([-6, 3])
    li_complex.append([9, 1])
    li_complex.append([-5, -2])


if __name__ == "__main__":
    start()
