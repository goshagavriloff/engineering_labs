from functools import wraps

class Decorator:
    @staticmethod
    def inputId(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result=None
            value=(input("Введите id:")).lstrip()

            if value.isdigit():
                kwargs['id'] = int(value)
                result = func(self, *args, **kwargs) 
            else:
                print("Неправильный формат id")
            return result
        return wrapper