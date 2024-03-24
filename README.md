# Mind Mentor App

The Mind Mentor app is a tool designed to provide mental health support and advice to users based on their current mood or mental state. It utilizes artificial intelligence powered by Google's Generative AI to generate personalized advice and techniques for managing various mental health issues.

## Features

- **Upload Image**: Users can upload an image related to their mood or mental state (optional).
- **Describe Feelings**: Users can describe their current mood or mental state using text (optional).
- **Get Mental Health Advice**: By clicking the "Get Mental Health Advice" button, users receive personalized advice and techniques for managing their current state.
- **Responsive Design**: The app is responsive and can be accessed from various devices.

## Installation

1. Clone the repository:
- https://github.com/missLaiba22/Gemini_Mind_Mentor.git
2. Install dependencies:
- pip install -r requirements.txt

3. Configure API key:
- Obtain a Google Generative AI API key and set it as an environment variable named `GOOGLE_API_KEY`.

4. Run the app:
- streamlit run Mind_Mentor.py

## Usage

1. Open the app in your web browser.
2. Upload an image related to your mood or describe your feelings in the text area.
3. Click the "Get Mental Health Advice" button.
4. Receive personalized advice and techniques for managing your current mood or mental state.

## Technologies Used

- [Streamlit](https://streamlit.io/): For building the web application.
- [Google Generative AI](https://cloud.google.com/ai-platform/training/docs/algorithms): For generating personalized advice using artificial intelligence.
- [Python](https://www.python.org/): Programming language used for backend development.
- [Pillow](https://python-pillow.org/): Python Imaging Library for image processing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
