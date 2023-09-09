'''class A:
    def __init__(self):
        print("this is A class constructor")
    def startBrowserA(self):
        print("A class method")
        print("starting browser")
class B:
    def __init__(self):
        print("this is B class constructor")
    def startBrowserB(self):
        print("B class method")
        print("starting browser")'''

'''import pages.login.abc
obj=pages.login.abc.C()
obj.mytesting()'''

from pages.login.abc import C
obj=C()
obj.mytesting()
