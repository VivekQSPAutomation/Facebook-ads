def decor(func):
    test = 5
    def wraps(*args, **kwargs):
        nonlocal test
        print(test)
        test = test + 5
        print(test)
        return func(" ".join(args))
    print(test)
    return wraps


@decor
def check(value):
    print(value)

check("vivek", "check")
