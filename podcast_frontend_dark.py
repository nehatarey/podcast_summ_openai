import streamlit as st
import modal
import json
import os

# Set theme to dark mode
st.set_page_config(page_title="Podcast Dashboard", page_icon=":microphone:", layout="wide", initial_sidebar_state="expanded")
st.markdown(
    """
    <style>
    .stApp {
      background-color: #1F1F1F; 
      color: #DCDCDC;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("Newsletter Dashboard")

    available_podcast_info = create_dict_from_json_files('.')

    # Left section - Input fields 
    st.sidebar.header("Podcast RSS Feeds")

    # Dropdown box
    st.sidebar.subheader("Available Podcasts Feeds")
    selected_podcast = st.sidebar.selectbox("Select Podcast", options=available_podcast_info.keys())

    if selected_podcast:
      
        podcast_info = available_podcast_info[selected_podcast]

        # Right section - Newsletter content
        st.header("Newsletter Content")

        # Display the podcast title
        st.subheader("Episode Title")
        st.write(podcast_info['podcast_details']['episode_title'])
        
        # Display the podcast summary and the cover image in a side-by-side layout
        col1, col2 = st.columns([7, 3])
        
        with col1:
            # Display the podcast episode summary  
            st.subheader("Podcast Episode Summary")
            st.write(podcast_info['podcast_summary'])
            
        with col2:
            st.image(podcast_info['podcast_details']['episode_image'], caption="Podcast Cover", width=300, use_column_width=True)

        # Display key moments
        st.subheader("Key Moments")
        key_moments = podcast_info['podcast_highlights']
        for moment in key_moments.split('\n'):
            st.markdown(f"<p style='margin-bottom: 5px;'>{moment}</p>", unsafe_allow_html=True)

    # User Input box  
    st.sidebar.subheader("Add and Process New Podcast Feed")
    url = st.sidebar.text_input("Link to RSS Feed")

    process_button = st.sidebar.button("Process Podcast Feed")
    st.sidebar.markdown("**Note**: Podcast processing can take upto 5 mins, please be patient.")

    if process_button:
        # Call API to process podcast
        podcast_info = process_podcast_info(url)
        
        # Display podcast info
        st.header("Newsletter Content")
        st.subheader("Episode Title")
        st.write(podcast_info['podcast_details']['episode_title'])
        
        col1, col2 = st.columns([7, 3])
        
        with col1:
             st.subheader("Podcast Episode Summary")
             st.write(podcast_info['podcast_summary'])
             
        with col2:
             st.image(podcast_info['podcast_details']['episode_image'], caption="Podcast Cover", width=300, use_column_width=True)
             
        st.subheader("Key Moments")
        key_moments = podcast_info['podcast_highlights']
        for moment in key_moments.split('\n'):
            st.markdown(f"<p style='margin-bottom: 5px;'>{moment}</p>", unsafe_allow_html=True)

# Helper functions            
def create_dict_from_json_files(folder_path):
    ...

def process_podcast_info(url):
   ...
   
if __name__ == '__main__':
    main()
