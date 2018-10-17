'''
Created on Oct 17, 2018

@author: Surendra
'''
class MySingleton(object):
    '''
    classdocs
    '''
    someValue = 10
    _shared_state = {}

    def __new__(self, params):
        '''
        Constructor
        '''
        obj = super(MySingleton, self).__new__(self)
        obj.__dict__ = self._shared_state
        return obj


if(__name__ == "__main__"):
    a = MySingleton(2)
    b = MySingleton(3)
    a.someValue = 20
    print(id(a), id(b), a.someValue, b.someValue)




