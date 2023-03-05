# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="a") as file:
#     file.write("\nSome new text")

# with open("new_my_file.txt", mode="w") as file:
#     file.write("\nSome new text")

class A:

    def __init__(self):
        self.a = 123

    def __enter__(self):
        return self

    def __exit__(self, *exc_type):
        print(type(exc_type))
        print(*exc_type)
        pass


with A() as a:
    a.a = 78
