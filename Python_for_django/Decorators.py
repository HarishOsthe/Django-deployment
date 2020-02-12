def new_decorator(func):
    def wrap_func():
        print("Code here before executing func")
        func()
        print("func() has been called")
    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function is in need of a decorator")

func_needs_decorator()
# func_needs_decorator = new_decorator(func_needs_decorator)

# func_needs_decorator()
# ------------------ Manually created decorators -----------------------
# def hello():
#     return "Hi osthe"

# def other(func):
#     print("Hello")
#     print(func())

# other(hello)
# --------------------------------------------------------------------
# def hello(name="osthe"):
#     print("The Hello()")

#     def greet():
#         return "inside greet()"
#     def welcome():
#         return "inside welcome()"

#     if name == 'osthe':
#         return greet
#     else:
#         return welcome

# x=hello()

# print(x())

# ---------------------------------------------------------------------
# s = 'Global Variable'

# def func():
#     # global s
#     # s=50
#     # print(s)
#     mylocal = 10
#     print(locals())
#     print(globals()['s'])


# func()
# # print(s)
# -------------------------------------------------------------------------
# def hello(name="osthe"):
#     return "hello" + name

# print(hello())

# mynewgreet = hello

# print(mynewgreet())