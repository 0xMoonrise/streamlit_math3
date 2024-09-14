import streamlit as st
dashboard = st.Page(
    "home.py", title="Home", default=True
)

notes = st.Page(
    "content/manager.py", title="Differential Equations"
)



pg = st.navigation({
    "Content": [dashboard, notes]
})

pg.run()




