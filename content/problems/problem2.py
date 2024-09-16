from utils.common import latex_eq
def content():
    import streamlit as st
    import time
    import numpy as np

    st.write("### Problem 2")
    st.write("This problem is the same as the previous one.")
    latex_eq(r"""
    y'=4-9x^2-6x^4;\, y(1)=0
    """)
    st.write("It just changes the initial value")
    latex_eq(r"""
    y      &= 4x-3x^3-x^6+C_3 \\
    0   &= 4(1)-3(1)^3-(1)^6+C_3 \\
    0   &= 4-3-1+C_3 \\
    0   &= 4-4+C_3 \\
    0   &= 0+C_3 \\
    0   &= C_3
    """)
    st.write("Particular solution when $C_3 = 0$")
    latex_eq(r"""
    y      &= 4x-3x^3-x^6 \\
    """)
    st.write("The verification is the same as the previous one.")
    st.write("Consult **Problem 1** to review all the steps we followed.")
