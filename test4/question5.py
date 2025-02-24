from datetime import datetime


def log_function(func):
    name = func.__name__
    def inner_log(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'{timestamp} - {name} called')
        result = func(*args, **kwargs)
        return result
    return inner_log


@log_function
def sun_of_digits(number_str):
    digits_sum = sum(map(int, number_str))
    return digits_sum


@log_function
def trans_int_to_str(int_list):
    return list(map(str, int_list))


@log_function
def multiply(vector1, vector2):
    if len(vector1) != len(vector2):
        print("不等长，无法计算")
        return -1
    else:
        return sum(map(lambda x, y: x * y, vector1, vector1))


if __name__ == "__main__":
    print(sun_of_digits("123"))
    print(trans_int_to_str([123, 345, 456]))
    print(multiply([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
