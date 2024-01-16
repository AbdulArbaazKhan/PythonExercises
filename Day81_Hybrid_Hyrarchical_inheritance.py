# TODO: Single Inheritance
# Simple a Classs derived from one class
# TODO: Multiple Inheritance
# More than one classes are derived from one class
# TODO: Multilevel Inheritance
# Class level increases --> B is derived from A and C is derived from B
# TODO: Hybrid Inheritance
# Some classes are derived from one and other class are made from derived class
# TODO: Hierarchical Inheritance
# Like an organzed order from top to bottom and every entity may have some other entities

# TODO: Hybrid Inheritance
class Baseclass:
    pass


class Derived1(Baseclass):
    pass


class Derived2(Baseclass):
    pass


class Derived3(Derived1, Derived2):
    pass


# TODO: Hierarchical Inheritance

class BaseClass:
    pass


class Child1(BaseClass):
    pass


class Child2(BaseClass):
    pass


class C1(Child1):
    pass

# You know about hierarchy that top one is CEO then few managers and then Associate managers
# See google pics for more understanding
