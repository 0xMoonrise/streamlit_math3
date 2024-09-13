import streamlit as st

dashboard = st.Page(
    "home.py", title="Home", default=True
)

notes = st.Page(
    "notes/notes.py", title="Notes"
)

pg = st.navigation({
            "Content": [dashboard, notes]
})


#pages = [st.Page(f"notes/{page}") for page in sorted(os.listdir('notes/'))]
#plots = [st.Page(f"plots/{page}") for page in sorted(os.listdir('plots/'))]

#pg = st.navigation({
#    "Notes":pages,
#    "Plots":plots
#})

pg.run()





