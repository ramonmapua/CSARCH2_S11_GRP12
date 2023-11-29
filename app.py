import streamlit as st
import memory as mem
import cache as cch

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

    if st.button("Create", type="primary"):
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

        memory['display_memory']()
