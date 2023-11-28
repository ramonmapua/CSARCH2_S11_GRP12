import random as rnd
import memory as mem
import cache as cch

cache_blocks = 32
cache_lines = 16
memory_blocks = 256

# Init Cache
cache = cch.create_cache(cache_blocks, cache_lines)

# Init Memory
memory = mem.create_memory(cache_lines, memory_blocks)

# # Fill memory sequential up 2n times
# mem_value = 0
# for mem_address in range(2 * cache_blocks * cache_lines):
#     if mem_address >= (memory_blocks * cache_lines):
#         break
#     memory['update_memory'](mem_address, mem_value)
#     if mem_value < (cache_blocks * 2) - 1:
#         mem_value += 1
#     else:
#         mem_value = 0

# Fill memory random up 4n times
for mem_address in range(4 * cache_blocks * cache_lines):
    if mem_address >= (memory_blocks * cache_lines):
        break

    mem_value = rnd.randint(0, 254)
    memory['update_memory'](mem_address, mem_value)  

cnt_miss = 0
cnt_hit = 0  

# Direct Mapping
for mem_address in range(memory_blocks * cache_lines):
    block_size = (memory_blocks * cache_lines) // memory_blocks
    # address / number of blocks
    cch_block = (mem_address // block_size) % cache_blocks
    # cache line of address (where it will go)
    cch_line = mem_address % cache_lines

    # store curren mem_address value
    mem_value = memory['access_memory'](mem_address)
    cch_value = cache['access_cache'](cch_block, cch_line)

    # # Debug Log
    # print("A: %04d, %04d" % ((mem_address // block_size), mem_address))
    # print("C: %04d, %04d" % (cch_block, cch_line))
    #print(str(cch_block) + ', ' + str(cch_line) + '\n')

    if mem_value != None:
        # if cache hit
        if cch_value != mem_value:
            # Do update cache
            cache['update_cache'](cch_block, cch_line, mem_value)
            cnt_miss += 1
            # print("")
        else:
            cnt_hit += 1
            # print("Cache Hit.\n")
    # else:
    #     print("")

print("Misses: %-4d" % (cnt_miss))
print("Hits: %-4d\n" % (cnt_hit))

cache['display_cache']()
