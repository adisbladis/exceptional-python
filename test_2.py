from exceptional import exceptional


@exceptional
def main():
    try:
        result = (1 == 1)
        assert result
    except AssertionError:
        pass
    else:
        raise Exception(1)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
