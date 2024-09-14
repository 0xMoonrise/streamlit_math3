import streamlit as st
import os


def dynamic_selectbox(path, message, placeholder):
    module_path = path.replace('/', '.')
    files = [file for file in sorted(os.listdir(path)) if file != '__pycache__']
    problems = {f'{message} {i}': file for i, file in enumerate(files, 1)}


    option = st.selectbox(
        'This is a test',
        problems.keys(),
        label_visibility='collapsed',
        index=None,
        placeholder=placeholder
    )

    if option:
        name, _ = os.path.splitext(problems.get(option))
        module_name = f'{module_path}{name}'
        module = __import__(module_name, fromlist=['content'])
        page = getattr(module, 'content')
        page()
