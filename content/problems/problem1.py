def content():
    import streamlit as st
    st.write("### Problem 1")
    st.write(r"""
    $$
    \begin{aligned}
    y'&=4-9x^2-6x^5; y(1) = 2 \\
    \end{aligned}
    $$
    Separating variables, with $y'$ set to $\frac{dy}{dx}$
    $$
    \begin{aligned}
    \frac{dy}{dx}&=4-9x^2-6x^5 \\
    dy &= 4-9x^2-6x^5 dx \\
    \end{aligned}
    $$""")
    with st.expander("**Fundamental property**"):
        st.success(r"""**Remeber:** $\frac{a}{b}c=d$, then $b\cdot\frac{a}{b}c=d\cdot b \,$ hence
        $\cancel{b}\cdot\frac{a}{\cancel{b}}c=d\cdot b $ $\rightarrow$ $a\cdot c = d \cdot b$""")
        st.write(r"In this case:")
        st.write(r"""
        $$
        \begin{aligned}
        \frac{dy}{dx}&=4-9x^2-6x^5 \\
        dx \cdot \frac{dy}{dx}&=4-9x^2-6x^5 \cdot dx \\
        \cancel{dx}\frac{dy}{\cancel{dx}} &=4-9x^2-6x^5 \cdot dx
        \end{aligned}
        $$
        """)
    st.write("Integrating on both sides")
    st.write(r"""
    $$
    \begin{aligned}
    \int{dy} &= \int{(4 - 9x^2-6x^5)dx}
    \end{aligned}
    $$
    """)
    st.write("Operating on the left-hand side:")
    st.write(r"""
    $$
    \begin{aligned}
    \int{dy} &= y + C_1
    \end{aligned}
    $$
    """)
    with st.expander("**Calculus property**"):
        st.success(r"""$\int{k\, dx} = kx+C$""")
        st.write("In this case:")
        st.write(r"""
        $$
        \begin{aligned}
        \int{1\,dy}&=1y+C_1 \\
        \int{dy} &= y + C_1
        \end{aligned}
        $$
        """)
        st.write(r"""**Remember:** If there's nothing preceding a variable on the **left side**, 
        it means there is an implicit **1**, such as: $1a = a$.
        """)
    st.write("Operating on the right-hand side:")
    st.write(r"""
    $$
    \begin{aligned}
    \int{(4-9x^2-6x^5)dx} &= \int{4dx}-\int{9x^2dx}-\int{6x^5dx} \\
                          &= 4x-\frac{9x^3}{3}-\frac{6x^6}{6}+C_2 \\
                          &= 4x-\frac{\cancel{9}x^3}{\cancel{3}}-\frac{\cancel{6}x^6}{\cancel{6}}+C_2\\
                          &= 4x-3x^3-x^6+C_2
    \end{aligned}
    $$
    """)
    with st.expander("**Calculus property**"):
        st.success(r"""$\int{(k\,\cdot u \pm w \cdot v )dx} = k\int{u\,dx}+w\int{v\,dx}+C$""")
        st.write("or")
        st.success(r"$\int{(ax+bx+cx)dx}=\int{ax\,dx}+\int{bx\,dx}+\int{cx\,dx}$")
        st.write("Exponential rule")
        st.success(r"$\int{u^n\,du}=\frac{u^{n+1}}{n+1}+C$")
    st.write("Hence, our **explicit general solution** will be")
    st.write(r"""
    $$
    \begin{aligned}
        y +C_1 &= 4x-3x^3-x^6+C_2 \\
        y      &= 4x-3x^3-x^6+C_3
    \end{aligned}
    $$
    where $C_3$ is $C_2-C_1$
    """)
    st.write("""#### Initial condition value""")
    st.write("""
    $$
    2 = 4(1)-3(1)^3-(1)^6+C_3
    $$
    where $y(1)=2$
    """)
    with st.expander("**Observation**"):
        st.success(r"$y(x)=y$ hence $y(1)=2$")
        st.write("where $x=1$ and $y=2$")
        st.write(r"$y = 4x-3x^3-x^6+C_3\\2 = 4(1)-3(1)^3-(1)^6+C_3$")
    st.write(r"""
    $$
    \begin{aligned}
    2 &= 4(1)-3(1)^3-(1)^6+C_3 \\
    2 &= 4-3-1 +C_3 \\
    2 &= 4-4 +C_3 \\
    2 &= 0 + C_3 \\
    2 &= C_3
    \end{aligned}
    $$
    """)
    st.write("Particular solution when $C_3=2$")
    st.write(r"""
    $$
        \underline{y = 4x-3x^3-x^6+2} \\
    $$
    """)
    with st.expander("**Comprobation**"):
        st.write(r"""
        $$
        \begin{aligned}
            y'            &= 4-9x^2-6x^5 \\
            \frac{dy}{dx} &= \frac{d}{dx}[4x-3x^3-x^6+2] \\
                          &= 4 -9x^2-6x^5
        \end{aligned}
        $$
        """)
