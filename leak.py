from memory.memory_leak import MemoryLeak

# Create an instance of the class
memory_leak_obj = MemoryLeak()

# Generate data, causing a memory leak
memory_leak_obj.generate_data()

# Clear the memory
memory_leak_obj.clear_memory()

# Generate data again
memory_leak_obj.generate_data()

# Print the length of the data list
print(len(memory_leak_obj.data))