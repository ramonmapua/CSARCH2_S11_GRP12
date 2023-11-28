import memory as mem
import cache as cch

cache_blocks = 32
cache_lines = 16
memory_blocks = 33

# Init Cache
cache = cch.create_cache(cache_blocks, cache_lines)

# Init Memory
memory = mem.create_memory(cache_lines, memory_blocks)

# Fill memory sequential
mem_value = 0
for mem_address in range(memory_blocks * cache_lines):
    memory['update_memory'](mem_address, mem_value)
    if mem_value < (cache_blocks * 2) - 1:
        mem_value += 1
    else:
        mem_value = 0

#memory['display_memory']()

cnt_miss = 0
cnt_hit = 0  

# Direct Mapping
for mem_address in range(memory_blocks * cache_lines):

    # store curren mem_address value
    mem_value = memory['access_memory'](mem_address)

    block_size = (memory_blocks * cache_lines) // memory_blocks
    # address / number of blocks
    cch_block = (mem_address // block_size) % cache_blocks
    # cache line of address (where it will go)
    cch_line = mem_address % cache_lines

    # Debug Log
    # print("A: %04d, %04d" % ((mem_address // block_size), mem_address))
    # print("C: %04d, %04d\n" % (cch_block, cch_line))
    #print(str(cch_block) + ', ' + str(cch_line) + '\n')
    
    if cache['access_cache'](cch_block, cch_line) == mem_value:
        cnt_hit += 1
        print("Cache Hit.")
    else:
        # Do update cache
        cache['update_cache'](cch_block, cch_line, mem_value)
        cnt_miss += 1
print("\n")

print("Misses:" + str(cnt_miss) + "\n")
print("Hits:" + str(cnt_hit) + "\n")

cache['display_cache']()
