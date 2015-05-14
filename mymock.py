#!/usr/bin/env python


class MyMock(object):

    """docstring for MyMock"""

    def __init__(self, spec=None, return_value=None):
        super(MyMock, self).__init__()
        self.method_calls = []
        self.spec = spec
        self.return_value = return_value

    def __getattr__(self, name):
        if name == 'test':
            self.method_calls.append(name)
            return self.func
        else:
            raise AttributeError

    def func(self, *agrs, **kw):
        pass


class Foo(object):
    # instance properties
    _fooValue = 123

    def callFoo(self):
        print "Foo:callFoo_"

    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue

test_mock = MyMock()
print test_mock

test_mock.test(spec=Foo, return_value='OK')
print test_mock.method_calls
