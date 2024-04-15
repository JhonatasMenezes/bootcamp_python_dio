import functools


def duplicate(func):
    @functools.wraps(func) # keep the __name__ attribute as the func name
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    
    return envelope


@duplicate
def learn(tecnology):
    print(f"Estou aprendendo {tecnology}")


learn("Python")
print(learn.__name__)