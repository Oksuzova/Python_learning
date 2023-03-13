# Pytest basics

# - Find test automatically
# - Test file names
    # must start with ‘test_*.py’
    # or
    # must end with ‘*_test.py
# Finds files in current directory and subdirectories


# Test files can have just function for classes
# If class, then ‘__init__()’ should not exist
# Functions must start with ‘test_*’
    # def test_foo_bar(arg1, arg2, ..):
# Class names must start with ‘Test’ and methods with ‘test_’
    # Class TestFooBar(object):
    # def test_verify_something():

# smoke_test.py
def test_user_login():
    print("log in")


def test_user_register():
    print("log in")


def test_user_logout():
    print("log in")

# smoke_test.py
Class TestUserSmoke(object):

    def test_user_login():
        print("log in")

    def test_user_register():
        print("log in")

    def test_user_logout():
        print("log in")
