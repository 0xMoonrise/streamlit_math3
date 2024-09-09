import streamlit as st
import numpy as np
import plotly.graph_objects as go


st.write("#### **Modeling a function**")

formula=r'''
$$
\begin{align*}
    \frac{{x^4}}{{4(x^2+1)}} + \frac{{x^2}}{{2(x^2+1)}} + \frac{{C}}{{(x^2+1)}}
\end{align*}
$$
'''
st.markdown(
    """
    <style>
    .stSelectbox div[data-baseweb="select"] > div:first-child {
        }
    </style>
    """,
    unsafe_allow_html=True
)
min, top =-10, 10
st.write(f"{formula}")

options = [i*(5/4) for i in range(min, top)]

option = st.selectbox(
    'How many functions do you want to model?',
    list(range(1, len(options)))
)

values = options[:option]

fig = go.Figure()
x=np.round(np.linspace(min, top, 100), 2)

def f(n):
    return np.round(((x**4) / (4 * (x**2 + 1))) + ((x**2) / (2 * (x**2 + 1))) + (n / (x**2 + 1)), 2)



for step in values:
    fig.add_trace(
        go.Scatter(
            visible=False,
            name=f"Step {step}",
            x=x,
            y=f(step)))

fig.data[0].visible = True

steps = []

for i in range(len(fig.data)):
    step = dict(method="update",
                args=[{"visible": [False] * len(fig.data)},
                      {"title": f"Slider switched to step: {i}"}])
    step["args"][0]["visible"][i] = True
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Frequency: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

st.plotly_chart(fig)

