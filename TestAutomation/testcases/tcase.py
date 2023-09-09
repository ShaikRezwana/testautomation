
#import libraryname.modulename-----Method1
'''import Library.commonmodule

objA=Library.commonmodule.A()
objA.startBrowserA()

objB=Library.commonmodule.B()
objB.startBrowserb()'''


# from libraryname.modulename import class name----Method2
from Library.commonmodule import A
objA=A()
objA.startBrowserA()