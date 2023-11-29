import streamlit as st
import memory as mem
import cache as cch
import random as rnd

# Assumed Constants
cache_blocks = 32
cache_lines = 16
memory_blocks = 0

# Time Constants
mem_access_time = 10 # Time to access memory (read or write)
cch_access_time = 1  # Time to access cache (read or write)
# miss penalty = cache check + memory read * # of words + cache read
miss_pen_time = cch_access_time + (cache_lines * mem_access_time) + cch_access_time

## streamlit page set-up
st.set_page_config(page_title="Group 12 Cache Project", page_icon=":floppy_disk:", layout="wide")

# Header Section
st.title("Cache Simulation Project")
st.subheader("CSARCH2 S11 Group 12")

# Project Section
with st.container():
    st.write("Cache blocks = ", cache_blocks)
    st.write("Cache line = ", cache_lines)
    st.write("Read policy = Non-Load Through")
    memory_blocks = st.number_input("Enter number of memory blocks: ", min_value=1, value=1, placeholder="Enter a number...")

    test_case = st.selectbox('Select a test case:', ('Empty', 'Test Case 1', 'Test Case 2', 'Test Case 3'), index=0)

    if st.button("Create and Simulate", type="primary"):
        st.divider()
        
        cache = cch.create_cache(cache_blocks, cache_lines)
        memory = mem.create_memory(cache_lines, memory_blocks)

        if test_case == 'Test Case 1':
            # Fill memory sequential up 2n times
            mem_value = 0
            for mem_address in range(2 * cache_blocks * cache_lines):
                if mem_address >= (memory_blocks * cache_lines):
                    break
                memory['update_memory'](mem_address, mem_value)
                if mem_value < (cache_blocks * 2) - 1:
                    mem_value += 1
                else:
                    mem_value = 0
        elif test_case == 'Test Case 2':
            # Fill memory random up 4n times
            for mem_address in range(4 * cache_blocks * cache_lines):
                if mem_address >= (memory_blocks * cache_lines):
                    break

                mem_value = rnd.randint(0, 254)
                memory['update_memory'](mem_address, mem_value)
        elif test_case == 'Test Case 3':
            mem_value = 0
            loops = 0
            for mem_address in range(4 * cache_blocks * cache_lines):
                if mem_address >= (memory_blocks * cache_lines):
                    break
                # 0 - 31
                if mem_value < cache_blocks - 1:
                    memory['update_memory'](mem_address, mem_value)
                    mem_value += 1
                # 32 - 63
                elif (mem_value >= cache_blocks - 1) & (mem_value < (cache_blocks * 2) - 1):
                    memory['update_memory'](mem_address, mem_value)
                    if loops < 1:
                        mem_value = 0
                        loops += 1
                    else:
                        mem_value += 1
                # 64+
                elif mem_value >= (cache_blocks * 2) - 1:
                    memory['update_memory'](mem_address, mem_value)
                    mem_value = 0
                    loops = 0    
                    

        # Initialize Counters
        cnt_mem_access = 0
        cnt_miss = 0
        cnt_hit = 0
        total_time = 0

        str_log = "Block, Line, Value\n"

        # Direct Mapping
        for mem_address in range(memory_blocks * cache_lines):
            block_size = (memory_blocks * cache_lines) // memory_blocks
            # address / number of blocks
            cch_block = (mem_address // block_size) % cache_blocks
            # cache line of address (where it will go)
            cch_line = mem_address % cache_lines

            mem_value = memory['access_memory'](mem_address)
            cch_value = cache['access_cache'](cch_block, cch_line)
            cnt_mem_access += 1

            str_log += "Address: {:>04}\n".format(str(mem_address))
            str_log += "M: ({:>04}, {:>04}), {:>04}\n".format(str((mem_address // block_size)), str(mem_address % cache_lines), str(mem_value))
            str_log += "C: ({:>04}, {:>04}), {:>04}\n".format(str(cch_block), str(cch_line), str(cch_value))
            

            # store curren mem_address value
            if mem_value != None:
                # if cache miss
                if cch_value != mem_value:
                    cache['update_cache'](cch_block, cch_line, mem_value)
                    cnt_miss += 1
                else:
                    str_log += "Cache Hit.\n"
                    cnt_hit += 1
            
            str_log += "\n"

        rate_hit = 0
        rate_miss = 0

        cnt_hmtotal = cnt_hit + cnt_miss
        if cnt_hmtotal > 0:
            rate_hit = cnt_hit / cnt_hmtotal
            rate_miss = cnt_miss / cnt_hmtotal
        ave_access_time = (rate_hit * cch_access_time) + (rate_miss * miss_pen_time)
        total_access_time = (cnt_hit * cch_access_time * cache_lines) + (cnt_miss * miss_pen_time)

        st.subheader("Simulation Stats")
        st.write("Memory Access Count: %-4d" % (cnt_hmtotal))
        st.write("Hits: %-4d (%3.2f%%)\n" % (cnt_hit, rate_hit * 100))
        st.write("Misses: %-4d (%3.2f%%)" % (cnt_miss, rate_miss * 100))
        st.write("Average Access Time: %4.0fns" % (ave_access_time))
        st.write("Total Access Time: %4.0fns" % (total_access_time))
        
        st.divider()

        memory['display_memory']()
        cache['display_cache']()
        with st.expander("See Path Trace"):
            st.code(str_log, line_numbers=True)
