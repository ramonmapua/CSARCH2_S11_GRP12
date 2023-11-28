from collections import deque

def create_memory(cache_line, memory_blocks):
    memory_size = cache_line * memory_blocks
    memory_queue = deque(maxlen=memory_size)

    # Fill memory with Zeroes
    initial_value = 0
    for _ in range(memory_blocks):
        memory_queue.append([initial_value] * cache_line)

    # Access Address in Memory
    # Zeroed Index
    def access_memory(address):
        if address < memory_size:
            block_index, offset = divmod(address, cache_line)
            return memory_queue[block_index][offset]
        else:
            raise ValueError("Address out of bounds")

    # Update Address in Memory
    def update_memory(address, value):
        if address < memory_size:
            block_index, offset = divmod(address, cache_line)
            memory_queue[block_index][offset] = value
        else:
            raise ValueError("Address out of bounds")

    # Display Entire Memory
    def display_memory():
        for block in memory_queue:
            print(block)

    # Dictionary of Functions
    return {
        'access_memory': access_memory,
        'update_memory': update_memory,
        'display_memory': display_memory
    }

# # Debugging
# cache_line_size = 16
# memory_block_count = 5

# memory = create_memory(cache_line_size, memory_block_count)

# # Test: Access memory
# memory['display_memory']()
# print("Value at address 5:", memory['access_memory'](5))

# # Test: Update Memory
# memory['update_memory'](5, 42)
# print("Updated value at address 5:", memory['access_memory'](5))
# memory['display_memory']()