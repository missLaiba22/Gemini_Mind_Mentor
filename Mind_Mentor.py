import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

# Load environment variables
load_dotenv()

# Configure GenAI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response
def get_gemini_response(input_prompt, image_uri=None):
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    if image_uri:
        # Use image URI in the prompt
        response = model.generate_content([image_uri, input_prompt])
    else:
        # Use text-only prompt
        response = model.generate_content([input_prompt])
    
    if hasattr(response, 'parts') and response.parts:
        return response.parts[0].text
    else:
        raise ValueError("Failed to generate a response. Please try again with a different input.")

# Function to upload image and get URI
def upload_image(image_bytes):
    # Temporarily save the image to upload
    with open("temp_image.png", "wb") as temp_file:
        temp_file.write(image_bytes)
    
    # Upload the file and get the URI
    sample_file = genai.upload_file(path="temp_image.png", display_name="Uploaded Image")
    
    # Remove the temporary file
    os.remove("temp_image.png")
    
    return sample_file.uri

# Function for the conversation with Mind Mentor
def mind_mentor_conversation():
    st.header("Mind Mentor - Conversation")

    # Upload an image related to mood or mental state
    uploaded_image = st.file_uploader(
        "Upload an image related to your mood or mental state (optional):",
        type=("jpg", "jpeg", "png"),
    )

    # Take a photo using the camera (optional)
    camera_image = st.camera_input("Take a photo related to your mood or mental state (optional):")

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        # Convert image to bytes and upload
        image_bytes = uploaded_image.read()
        
        try:
            image_uri = upload_image(image_bytes)
            st.write(f"Image URI: {image_uri}")
        except Exception as e:
            st.error(f"Error uploading image: {str(e)}")
            image_uri = None
    elif camera_image is not None:
        if isinstance(camera_image, BytesIO):
            image = Image.open(camera_image)
            st.image(image, caption="Captured Image.", use_column_width=True)

            # Convert image to bytes and upload
            image_bytes = camera_image.getvalue()
            
            try:
                image_uri = upload_image(image_bytes)
                st.write(f"Image URI: {image_uri}")
            except Exception as e:
                st.error(f"Error uploading image: {str(e)}")
                image_uri = None
        else:
            st.error("Unsupported type for camera image.")
            image_uri = None
    else:
        image_uri = None

    # Text area for describing current mood or mental state
    input_prompt = st.text_area(
        "Describe your current mood or mental state (optional):",
        height=100,
        max_chars=500,
    )

    # Button to get mental health advice
    submit = st.button("Get Mental Health Advice")

    if submit:
        st.info(
            """
            **Disclaimer:** This app is designed to provide general support and cannot replace professional help. If you're struggling with serious mental health issues, please reach out to a qualified therapist or counselor. Here are some resources that can help:
            - National Suicide Prevention Lifeline: 988
            - Crisis Text Line: Text HOME to 741741
            - SAMHSA National Helpline: 1-800-662-HELP (4357)
            """
        )

        if not input_prompt and image_uri is None:
            st.warning("Please describe your feelings or upload an image to receive advice.")
            return

        if image_uri:
            prompt = f"Analyze the user's mood based on the image provided and the description: {input_prompt}. Offer supportive advice and techniques for managing their current state."
        else:
            prompt = f"The user describes their mood or mental state as: {input_prompt}. Offer supportive advice and techniques for managing their current state."

        try:
            response = get_gemini_response(prompt, image_uri)
            st.header("Mind Mentor's Advice:")
            st.write(response)
        except ValueError as e:
            st.error(str(e))

# Main part of the application
st.set_page_config(page_title="Mind Mentor", page_icon=":brain:")  # Set page title and icon
# Add logo to top left corner
st.sidebar.image("logo.jpg", use_column_width=True)
st.markdown(
    """
    <style>
    .stApp {
        max-width: 800px;  /* Set maximum width for content */
        margin: auto;      /* Center content horizontally */
    }
    .stButton button {
        background-color: #4CAF50;  /* Set button background color */
        color: white;                /* Set button text color */
        border: none;                /* Remove button border */
        padding: 10px 20px;          /* Add padding to button */
        text-align: center;          /* Center button text */
        text-decoration: none;       /* Remove underline from button text */
        display: inline-block;       /* Make button a block element */
        font-size: 16px;             /* Set font size for button text */
        margin: 4px 2px;             /* Add margin around button */
        cursor: pointer;             /* Add cursor pointer on hover */
        border-radius: 8px;          /* Add border radius to button */
    }
    </style>
    """,
    unsafe_allow_html=True,
)  # Add custom CSS for styling

mind_mentor_conversation()
