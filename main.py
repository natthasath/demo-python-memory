from memory.memory_type import MemoryType

# Create an instance of the class
my_obj = MemoryType("arg1_value", "arg2_value")

# Call the method to modify the instance variable
my_obj.method()

# Print the values of the variables
print(MemoryType.class_variable) # Static variable
print(my_obj.arg1) # Stack variable
print(my_obj.arg2) # Stack variable
print(my_obj.instance_variable) # Heap variable