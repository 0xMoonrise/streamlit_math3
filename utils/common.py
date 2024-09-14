import streamlit as st
import os


def dynamic_selectbox(path, message, placeholder, label):
    module_path = path.replace('/', '.')
    files = [file for file in sorted(os.listdir(path)) if file != '__pycache__']
    problems = {f'{message} {i}': file for i, file in enumerate(files, 1)}


    option = st.selectbox(
        label,
        problems.keys(),
        index=None,
        placeholder=placeholder
    )

    if option:
        name, _ = os.path.splitext(problems.get(option))
        module_name = f'{module_path}{name}'
        module = __import__(module_name, fromlist=['main'])
        page = getattr(module, 'main')
        page()
