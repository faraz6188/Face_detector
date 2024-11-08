import streamlit as st
import subprocess
import threading

def run_app(app_name):
    """Function to run a Streamlit app using subprocess."""
    subprocess.run(["streamlit", "run", app_name])


st.markdown(
    """
    <style>
    /* Global styles */
    body {
        font-family: 'Arial', sans-serif;
    }

    /* Center align the title */
    .title {
        text-align: center;
        color: #6600cc; /* A nice purple color */
        font-size: 60px; /* Larger font size */
        margin-top: 20px;
        margin-bottom: 60px; /* Space below the title */
    }

    /* Style the sidebar */
    .css-1aumxhk {
        background-color: #f0f4f8 !important; /* Light sidebar background */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    /* Style buttons */
    .stButton > button {
        background-color: #6600cc; /* purple background for buttons */
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .stButton > button:hover {
        color: white;
        background-color: green; /* light pruple on hover */
        border-style: solid;
        border-color: black;
    }

    </style>
    """,
    unsafe_allow_html=True
)
# Title of the main app
st.markdown("<h1 class='title'>Faraz's CNN Web Application Project</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Button for launching App 1
with col1:
    if st.button("Upload Image for detecting the Face"):
        st.write("Launching Image detection ...")
    # Start a new thread to run App 1
        threading.Thread(target=run_app, args=("detect_img.py",)).start()

# Button for launching App 2
with col2:
    if st.button("WebCame Face Detection"):
        st.write("Launching Face detection ...")
    # Start a new thread to run App 2
        threading.Thread(target=run_app, args=("scan.py",)).start()

# Optional: A message for when no app is selected
st.write("Click a button to launch an application.")

