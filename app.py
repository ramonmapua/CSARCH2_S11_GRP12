import streamlit as st

st.set_page_config(page_title="Group 12 Cache Project", page_icon=":floppy_disk:")

# Header Section
st.title("Cache Simulation Project")
st.subheader("CSARCH2 S11 Group 12")

# Project Section
with st.container():
    cache_blocks = 32
    cache_line = 16
    st.write("Cache blocks = ", cache_blocks)
    st.write("Cache line = ", cache_line)
    st.write("Read policy = Non-Load Through")
    memory_blocks = st.number_input("Enter number of memory blocks: ", min_value=1, value=None, placeholder="Enter a number...")
