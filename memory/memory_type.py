class MemoryType:
    # Static variable
    class_variable = "This is a class variable"

    def __init__(self, arg1, arg2):
        # Stack variable
        self.arg1 = arg1
        self.arg2 = arg2
        # Heap variable
        self.instance_variable = []

    def method(self):
        # Stack variable
        local_variable = "This is a local variable"
        # Append to the heap variable
        self.instance_variable.append("This is an instance variable")