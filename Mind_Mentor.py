import streamlit as st
import google.generativeai as genai
<<<<<<< HEAD
# import google_ai_generativelanguage
=======
>>>>>>> 1c1e22be03fd0af6798efba33cde7a1cf3b6fd8b
import os
from dotenv import load_dotenv
from PIL import Image  # Import the Image module

# Load environment variables
load_dotenv()

# Configure GenAI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response
def get_gemini_response(input_prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input_prompt])
    if hasattr(response, 'parts') and response.parts:
        return response.parts[0].text
    else:
        raise ValueError("Failed to generate a response. Please try again with a different input.")

# Function for the conversation with Mind Mentor
def mind_mentor_conversation():
    st.header("Mind Mentor - Conversation")

    # Upload an image related to mood or mental state
    uploaded_image = st.file_uploader(
        "Upload an image related to your mood or mental state (optional):",
        type=("jpg", "jpeg", "png"),
    )

    try:
        # Display the uploaded image
        if uploaded_image is not None:
            image = Image.open(uploaded_image)  # Use Image.open to open the uploaded image
            st.image(image, caption="Uploaded Image.", use_column_width=True)
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")

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

        if not input_prompt:
            st.warning("Please describe your feelings to receive advice.")
            return

        if uploaded_image is not None:
            prompt = f"You are a trained therapist. Analyze the user's mood based on the image and the provided description (optional). Offer supportive advice and techniques for managing their current state."
        else:
            prompt = f"You are a trained therapist. The user describes their mood or mental state as: {input_prompt}. Offer supportive advice and techniques for managing their current state."

        try:
            if uploaded_image is not None:
                response = get_gemini_response(input_prompt)
                st.header("Mind Mentor's Advice:")
                st.write(response)
            else:
                st.warning("Please upload an image related to your mood or mental state.")
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
