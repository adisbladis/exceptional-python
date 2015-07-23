from exceptional import exceptional


@exceptional
def good_method():
    raise Exception(1)

if __name__ == '__main__':
    try:
        good_method()
    except Exception as e:
        print(e)
