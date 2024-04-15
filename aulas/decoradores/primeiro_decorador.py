def my_decorator(function):
    def envelope():
        print("Faz algo antes de executar")
        function()
        print("Faz algo depois de executar")
    
    return envelope

@my_decorator
def hello_world():
    print("Olá mundo!")

hello_world()
