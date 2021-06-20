import plugins

@plugins.register
def greet(name):
    print(f"Hello {name}, how are you today?")

# greeter/howdy.py
import plugins

@plugins.register
def greet(name):
    print(f"Howdy good {name}, honored to meet you!")

# greeter/yo.py
import plugins

@plugins.register
def greet(name):
    print(f"Yo {name}, good times!")