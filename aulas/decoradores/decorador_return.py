def my_decorator(func):
    def envelope(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    
    return envelope


@my_decorator
def hello(name, another_arg):
    print(f'Olá mundo, eu sou o {name}!')
    return another_arg.upper()


result = hello("Jhonatas", "retorno minusculo")
print(result)
