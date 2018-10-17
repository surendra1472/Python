def single(data):
    if data == True:
        return singleton
    else:
        return normal


def singleton(cls):
    instances = {}

    def wrapper(*a, **b):
        print(instances)
        if cls not in instances:
            instances[cls] = cls(*a, **b)
        return instances[cls]

    return wrapper


def normal(cls):
    def wrapper(*a, **b):
        return cls(*a, **b)

    return wrapper


@single(True)
class MySingletonWithDecorator:
    def __init__(self, value):
        self.someValue = value
        print value


if(__name__=="__main__"):
    aSingle = MySingletonWithDecorator(2)
    bSingle = MySingletonWithDecorator(3)
    aSingle.someValue = 20
    print(id(aSingle), id(bSingle), aSingle.someValue, bSingle.someValue)
