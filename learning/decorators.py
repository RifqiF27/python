def announce(f):
    def wrapper():
        print(1)
        f()
        print(3)
    return wrapper


@announce
def hello():
    print(2)
    
hello()