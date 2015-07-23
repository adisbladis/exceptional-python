from exceptional import exceptional, NoExceptionError


class Fizzable(Exception):
    pass


class Buzzable(Exception):
    pass


class FizzBuzzable(Exception):
    pass


@exceptional
def handle(x):
    div_3 = (x % 3 == 0)
    div_5 = (x % 5 == 0)
    if div_3 and div_5:
        raise FizzBuzzable()
    if div_3:
        raise Fizzable()
    if div_5:
        raise Buzzable()


for x in range(1, 101):
    try:
        handle(x)

    except FizzBuzzable:
        print('Fizzbuzz')

    except Fizzable:
        print('Fizz')

    except Buzzable:
        print('Buzz')

    except NoExceptionError:
        print(x)
