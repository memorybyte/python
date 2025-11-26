# Duck typing is a programming concept where the type or class of an object is less important than the methods and properties it has. 
# The name comes from the phrase:
"If it walks like a duck and quacks like a duck, then it must be a duck."

# Runtime flexibility: Python doesn't require objects to inherit from a common base class or implement a specific interface - they just need to have the required methods.

# With duck typing, you skip the explicit interface/base class entirely. The object just needs to "quack" (have the method) when called.

class TextBox:
    def draw(self):
        print('TextBox')


class DropDownList:
    def draw(self):
        print('DropDownList')

# duck typing
def draw(controls):
    for control in controls:
        control.draw()

draw([TextBox(), DropDownList()])
