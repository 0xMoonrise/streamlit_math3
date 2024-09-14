import streamlit as st
import os
import utils.common as com

st.write("""
# Welcome to Differential Equation Notes

In this section, we will explore the knowledge we acquired from our Math 3 classes. We will highlight even the most basic properties, regardless of their application, and explain how to solve problems in calculus, algebra, trigonometry, and arithmetic. 

**Note**: The following content has been taken from our 18 homework problems.

Please select the problem you want to dive into.
""")

com.dynamic_selectbox('content/problems/', 'Problem', 'Choose a problem')
