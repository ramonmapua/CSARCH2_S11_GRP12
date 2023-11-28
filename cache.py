from collections import deque

def create_cache(cache_blocks, cache_lines):
    cache_queue = deque(maxlen=cache_blocks)

    # Initialize with Zeroes
    initial_value = 0
    for _ in range(cache_blocks):
        cache_queue.append([initial_value] * cache_lines)

    # Access Block, Line on Cache
    # Zeroed Index, on both block and cache
    def access_cache(block_index, line_index):
        if block_index < cache_blocks and line_index < cache_lines:
            return cache_queue[block_index][line_index]
        else:
            raise ValueError("Invalid cache block or line index")

    # Update Block, Line on Cache
    def update_cache(block_index, line_index, value):
        if block_index < cache_blocks and line_index < cache_lines:
            cache_queue[block_index][line_index] = value
        else:
            raise ValueError("Invalid cache block or line index")

    # Display Entire Cache
    def display_cache():
        for block in cache_queue:
            print(block)

    # Dictionary of Functions
    return {
        'access_cache': access_cache,
        'update_cache': update_cache,
        'display_cache': display_cache
    }

# # Example usage:
# cache_block_count = 32  # Replace with your desired number of cache blocks
# cache_line_count = 16  # Replace with your desired number of cache lines

# cache = create_cache(cache_block_count, cache_line_count)

# # Example: Access and update cache
# cache['display_cache']()
# print("Value at cache block 1, line 2:", cache['access_cache'](1, 2))

# cache['update_cache'](1, 2, 42)
# print("Updated value at cache block 1, line 2:", cache['access_cache'](1, 2))
# cache['display_cache']()