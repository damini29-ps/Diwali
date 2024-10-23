import streamlit as st

# Set a title
#st.title("Video Player Example")

# Display a video from a local file
video_file = open('Diwali.mp4', 'rb')
video_bytes = video_file.read()

# Streamlit video player
st.video(video_bytes)

