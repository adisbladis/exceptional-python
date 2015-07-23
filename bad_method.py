from exceptional import exceptional


@exceptional
def bad_method():
    return 1


if __name__ == '__main__':
    bad_method()
