import streamlit as st
import memory as mem
import cache as cch
import random as rnd

cache_blocks = 32
cache_lines = 16
memory_blocks = 0

## streamlit page set-up
st.set_page_config(page_title="Group 12 Cache Project", page_icon=":floppy_disk:")

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
                    mem_value += 1
                # 32 - 63
                elif (mem_value > cache_blocks - 1) & (mem_value < (cache_blocks * 2) - 1):
                    if loops < 2:
                        mem_value = 0
                        loops += 1
                    else:
                        mem_value += 1
                # 64+
                else:
                    mem_value = 0
                    loops = 0
                

                memory['update_memory'](mem_address, mem_value)

        # Initialize Counters
        cnt_mem_access = 0
        cnt_cch_access = 0
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
            if mem_value != None:
                mem_value = memory['access_memory'](mem_address)
                cnt_mem_access += 1
                cch_value = cache['access_cache'](cch_block, cch_line)
                cnt_cch_access += 1

                # if cache miss
                if cch_value != mem_value:
                    cache['update_cache'](cch_block, cch_line, mem_value)
                    cnt_cch_access += 1
                    cnt_miss += 1
                else:
                    cnt_hit += 1

        # Time Constants
        mem_access_time = 1
        cch_access_time = 1
        miss_pen_time = 10

        cnt_hmtotal = cnt_hit + cnt_miss
        rate_hit = cnt_hit / cnt_hmtotal * 100
        rate_miss = cnt_miss / cnt_hmtotal * 100
        ave_access_time = rate_hit * cch_access_time + (100 - rate_hit) * miss_pen_time

        st.subheader("Simulation Stats")
        st.write("Memory Access Count: %-4d" % (cnt_mem_access))
        st.write("Hits: %-4d (%3.2f%%)\n" % (cnt_hit, rate_hit))
        st.write("Misses: %-4d (%3.2f%%)" % (cnt_miss, rate_miss))
        st.write("Average Access Time: %4.0fns" % (ave_access_time))
        
        st.divider()

        memory['display_memory']()
        cache['display_cache']()
