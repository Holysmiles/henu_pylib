def calc(operation):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '**': lambda x, y: x ** y,
    }

    op_func = operations.get(operation)
    if not op_func:
        return lambda x, y: "错误操作"
    return op_func

if __name__ == "__main__":
    print(calc("+")(1, 3))
    print(calc("-")(1, 3))
    print(calc("*")(1, 3))
    print(calc("/")(1, 3))
    print(calc("**")(1, 3))

