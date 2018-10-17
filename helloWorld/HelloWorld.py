
class HelloWorld:

    def __init__(self, name):
        self.sayHello(name)

    def sayHello(self, name):
        print("Hello {0}".format(name))


if(__name__ == "__main__"):
    helloWorld = HelloWorld("World")
    helloWorld = HelloWorld("Lucy")
