# CLOSURE

# Try to explain it in plain English:
# Factory() is basically giving the widget function inside a different name because
# the return widget at the end makes factory() an instance of the widget method + values variable

# Try to explain it in pseudocode:
# Invocation of factory() -> returns a widget function + scoped data
# Since the function is asking for an argument, you must give factory() an argument, making it factory()(arg)

def factory():
    values = []
    def widget(value):
    	# print(value)
        values.append(value)
        return values
    return widget

worker = factory()
print(worker) # This returned widget method
worker(1)
worker(2)
print(worker(4))


# There is one work instance. 
# We are calling that instance's widget function 3 times within that instance, appending values to local values variable inside worker instance.
# Higher-order functions (functions can accept other functions as arguments and return functions to the caller)
# Nested function
# Closure