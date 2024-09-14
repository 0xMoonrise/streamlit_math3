import streamlit as st
import os
import utils.common as com

st.write("""
# Welcome to notes
In this section, we are going to explore the knowledge that we acquired from our Math 3 classes. 

Please select the topic you wish to explore
""")

com.dynamic_selectbox('notes/problems14/', 'AAAA', 'Choose a problem', 'Problem')

