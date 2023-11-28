from contextlib import contextmanager
from io import StringIO
from streamlit.scriptrunner.script_run_context import SCRIPT_RUN_CONTEXT_ATTR_NAME
from threading import current_thread
import sys
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
    memory_blocks = st.number_input("Enter number of memory blocks: ", min_value=1, value=None, placeholder="Enter a number...")
    if st.button("Start", type="primary"):
        cache = cch.create_cache(cache_blocks, cache_lines)
        memory = mem.create_memory(cache_lines, memory_blocks)

@contextmanager
def st_redirect(src, dst):
    placeholder = st.empty()
    output_func = getattr(placeholder, dst)

    with StringIO() as buffer:
        old_write = src.write

        def new_write(b):
            if getattr(current_thread(), SCRIPT_RUN_CONTEXT_ATTR_NAME, None):
                buffer.write(b)
                output_func(buffer.getvalue())
            else:
                old_write(b)

        try:
            src.write = new_write
            yield
        finally:
            src.write = old_write

@contextmanager
def st_stdout(dst):
    with st_redirect(sys.stdout, dst):
        yield

@contextmanager
def st_stderr(dst):
    with st_redirect(sys.stderr, dst):
        yield

with st_stdout("code"):
    print("Prints as st.code()")