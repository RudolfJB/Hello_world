# use main to ask user to use smily face as hello and sad face as goodbuy
def main():

    # Ask user to Type :) for a smily face
    smily_face = (input("Type ':)' to show you are happy "))

    # convert :) to emoji smily face
    convert()
    (":)", "😀")

    print(f"hello, {smily_face}")

    # Ask user to Type ()) for a sad face
    sad_face = (input("Type ':(' to show you are sad "))

    # convert :( to emoji sad face
    convert = (":(", "😒")

    print(f"goodbuy, {sad_face}")


def smily_face(h):
    return h


def sad_face(s):
    return s


def convert(c):
    return c


# end with main
main()
