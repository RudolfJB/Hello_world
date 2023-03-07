
# use main to ask user to use smily face as hello and sad face as goodbuy
def main():

    # Ask user to Type :) for a smily face
    smily_face = input("Type :) to show you are happy ")

    # convert :) to emoji smily face
    smily_face = smily_face.replace(":)", "😀")

    print(f"hello, {smily_face}")

    # Ask user to Type ()) for a sad face
    sad_face = input("Type :( to show you are sad ")

    # convert :( to emoji sad face
    sad_face = sad_face.replace(":(", "😒")

    print(f"goodbuy, {sad_face}")


# end with main
main()
