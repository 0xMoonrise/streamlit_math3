def main():
    import streamlit as st
    import time
    import numpy as np

#    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    st.write(
        """
        This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!
"""
    )
    st.sidebar.write('test')
    option = st.sidebar.selectbox(
    "**Problems homework 1.4:**",
    [f'opt {n}' for n in range(1, 4)],
    index=None,
    placeholder="Choose a problem"
    )
    st.write(f'you selected {option}')
