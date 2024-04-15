def duplicate(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    
    return envelope


@duplicate
def learn(tecnology):
    print(f"Estou aprendendo {tecnology}")


learn("Python")
