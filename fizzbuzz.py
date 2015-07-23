from exceptional import *

int = exceptionalize(int)


class Fizzable(Exception):
    pass


class Buzzable(Exception):
    pass


class FizzBuzzable(Exception):
    pass


@exceptional
def handle(x):
    try:
        (int(x % 3) == int(0))
    except TrueException:
        try:
            (int(x % 5) == int(0))
        except TrueException:
            raise FizzBuzzable()
        except FalseException:
            raise Fizzable()
    except FalseException:
        pass

    try:
        (int(x % 5) == int(0))
    except TrueException:
        raise Buzzable()
    except FalseException:
        pass


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
