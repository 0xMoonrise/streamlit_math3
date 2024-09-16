from utils.common import latex_eq

def content():
    import streamlit as st
    st.write("### Problem 3")
    latex_eq(r"""
    \frac{dy}{dx} &= \frac{6x-12}{x^2};\,y(1)=20
    """)
    with st.expander("**Fundamental property**"):
        st.success(r"""**Remeber:** $\frac{a}{b}c=d$, then $b\cdot\frac{a}{b}c=d\cdot b \,$ hence $\,
        \cancel{b}\cdot\frac{a}{\cancel{b}}c=d\cdot b $ $\rightarrow$ $a\cdot c = d \cdot b$""")
        st.write(r"In this case:")
        latex_eq(r"""
        \frac{dy}{dx}          &= \frac{6x-12}{x^2} \\
        dx \cdot \frac{dy}{dx} &= \frac{6x-12}{x^2} \cdot dx \\
        \cancel{dx}\frac{dy}{\cancel{dx}} &= \frac{6x-12}{x^2}  dx
        """)
    st.write("Integrating on both sides")
    latex_eq(r"""
    \int{dy}=\int{\frac{6x-12}{x^2}dx}
    """)
        
    with st.expander("**Distributive Property**"):
        st.success(r"""
        $ab+ac=a(b+c)$
        """)
        st.write("""
        In this case:
        """)
        st.write(r"""
        $$
        \frac{6\cdot x-6\cdot 2}{x^2} \\
        $$

        $$
        \frac{6(x-2)}{x^2}
        $$
        """)
    latex_eq(r"""
        \int{dy}=\int{\frac{6(x-2)}{x^2}dx}
    """)
    with st.expander("**Calculus Property**"):
        st.success(r"$\int{k\cdot\,x\,dx}=k\cdot\,\int{x\,dx}$")
        st.write(r"where $k$ is a constant $k \in \reals$")
    latex_eq(r"""
        \int{dy}=6\int{\frac{(x-2)}{x^2}dx}
    """)    
    st.write("Operating on the left-hand side:")
    
    
    
    
