def calculate_sum(*args):
    """
    Calculates sum of multiple numbers.
    """
    return sum(args)

print(calculate_sum(1, 2, 3, 4))


def print_student_info(**kwargs):
    """
    Prints student information.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_student_info(name="Ali", age=19, major="IT")
