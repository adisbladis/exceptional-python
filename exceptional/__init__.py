from functools import wraps


class NoExceptionError(Exception):
    pass


class TrueException(Exception):
   pass


class FalseException(Exception):
   pass


def _raise_true_or_false(a):
   if a:
      raise TrueException
   else:
      raise FalseException


def exceptional(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except Exception:
            raise
        else:
            raise NoExceptionError(result)

    return wrapper


class ExceptionalClass(object):

    def __getattribute__(self, name):
        real = super(ExceptionalClass, self).__getattribute__(name)
        if hasattr(real, '__call__'):
            return exceptional(real)
        return real


def exceptionalize(t):
    '''
    Make type exceptional
    '''

    class ExceptionalType(t):
        def __eq__(self, other):
            _raise_true_or_false(super(ExceptionalType, self).__eq__(other))

        def __lt__(self, other):
            _raise_true_or_false(super(ExceptionalType, self).__lt__(other))

    return ExceptionalType
