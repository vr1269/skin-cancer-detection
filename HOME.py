import streamlit as st
import streamlit.components.v1 as components

# Set page title
st.set_page_config(
    page_title="CarcinoSKin AI",
    page_icon="🧬",
    initial_sidebar_state="expanded",
)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(8vw, 20px);
            font-weight: 700;
            top: 0px;
            right: 25%;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,#FF4C4B, #FFFB80);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
    </style>
    <p id="effect">CarcinoSKin AI</p>
    """,
    height=69,
)


def page_layout():
    st.write("CarcinoSKin is an app that combines various ML models into one in order to determine if you have a disease, using CNN images of the patients. The app uses advanced algorithms to diagnose various diseases, including skin cancer.")
    st.markdown("## Benefits:")
    st.write("- Fast and accurate diagnosis of diseases")

    st.write("- Accessible from anywhere, anytime")
    st.markdown("## Why is our app unique?")
    st.write("- CarcinoSKin combines multiple ML models into one app")
   
    st.write("- CarcinoSKin uses advanced algorithms to provide fast and accurate diagnosis")
    st.markdown("## Relevance:")
 
    st.write("- The app can be used by doctors, hospitals, and patients")
    st.write("- CarcinoSKin can improve the accuracy and speed of disease diagnosis")
    st.markdown("## Uses:")
    st.write("- Hospitals and clinics can use CarcinoSKin to diagnose diseases more quickly")
    st.write("- Patients can use CarcinoSKin to get a quick and accurate diagnosis without the need for invasive procedures")
    
# Render page layout
page_layout()
