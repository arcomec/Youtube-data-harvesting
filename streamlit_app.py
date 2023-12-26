import streamlit as st
from googleapiclient.discovery import build

def main():
    st.title("YouTube Channel Migration Tool")

    # User input for YouTube channel ID
    channel_id = st.text_input("Enter YouTube Channel ID")

    if st.button("Get Channel Details"):
        if channel_id:
            # Set your API key
            api_key = "AIzaSyBZxXHtLkIraQoRHhYITbbexm5mAv7rGCE"  # Replace with your actual API key

            # Create a service object
            youtube = build("youtube", "v3", developerKey=api_key)

            try:
                # Make a request to the YouTube Data API
                request = youtube.channels().list(
                    part="snippet,contentDetails,statistics",
                    id=channel_id  # Use the user-input channel_id
                )
                response = request.execute()

                # Display channel details using st.write()
                if 'items' in response and response['items']:
                    channel_title = response['items'][0]['snippet']['title']
                    st.write(f"Channel Title: {channel_title}")
                    # Display other channel details as needed
                else:
                    st.warning("Channel details not found.")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

        else:
            st.warning("Please enter a YouTube Channel ID")

    # Checkbox to select channels for migration
    st.markdown("### Select Channels for Migration")
    channels_selected = st.checkbox("Select this channel for migration")

    if channels_selected:
        st.success("Channel selected for migration!")

if __name__ == "__main__":
    main()
