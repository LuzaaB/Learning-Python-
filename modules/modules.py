# "import" is needed to use modules
import sys
import modules_test
dir(sys) # to see whatever is there inside a module
dir() # for current module
dir(modules_test)
modules_test.say_hi()
print('Version',modules_test.__version__)