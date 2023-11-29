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
        memory['display_memory']()
