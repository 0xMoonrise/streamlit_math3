from utils.common import latex_eq

def content():
    import streamlit as st
    st.write("### Problem 3")
    st.write(latex_eq(r"""
    \frac{dy}{dx} &= \frac{6x-12}{x^2};\,y(1)=20
    """))
    with st.expander("**Fundamental property**"):
        st.success(r"""**Remeber:** $\frac{a}{b}c=d$, then $b\cdot\frac{a}{b}c=d\cdot b \,$ hence $\,
        \cancel{b}\cdot\frac{a}{\cancel{b}}c=d\cdot b $ $\rightarrow$ $a\cdot c = d \cdot b$""")
        st.write(r"In this case:")
        st.write(latex_eq(r"""
        \frac{dy}{dx}          &= \frac{6x-12}{x^2} \\
        dx \cdot \frac{dy}{dx} &= \frac{6x-12}{x^2} \cdot dx \\
        \cancel{dx}\frac{dy}{\cancel{dx}} &= \frac{6x-12}{x^2}  dx
        """))
    st.write("Integrating on both sides")
    st.write(latex_eq(r"""
    \int{dy}=\int{\frac{6x-12}{x^2}dx}
    """))
    st.write()
