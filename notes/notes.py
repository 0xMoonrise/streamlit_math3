import streamlit as st
import os

st.write("""
# Welcome to notes
In this section, we are going to explore the knowledge that we acquired from our Math 3 classes. 

Please select the topic you wish to explore
""")

files = [file for file in sorted(os.listdir('notes/problems14/')) if file != '__pycache__']
problems = {f'Problem {i}': file for i, file in enumerate(files, 1)}


option = st.selectbox(
    "**Problems homework 1.4:**",
    problems.keys(),
    index=None,
    placeholder="Choose a problem"
)

if option:
    name, _ = os.path.splitext(problems.get(option))
    module_name = f'notes.problems14.{name}'
    module = __import__(module_name, fromlist=['main'])
    page = getattr(module, 'main')
    page()
