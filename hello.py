print("hello world")


def hello():
    print("love you lots")


hello()


# my first OOP


class my_OOP():
    def __init__(self, **kw):
        super(my_OOP, self).__init__(**kw)

    def print_this(self, val):
        print(val)

    def main(self):
        val = input(">>")
        self.print_this(val)


my = my_OOP()

my.main()
