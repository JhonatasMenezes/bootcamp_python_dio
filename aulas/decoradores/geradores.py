def my_generator(numbers):
    
    for number in  numbers:
        yield number * 2



for i in my_generator([1, 2, 3, 4, 5]):
    print(i)