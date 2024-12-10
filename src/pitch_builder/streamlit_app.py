# src/latest_ai_development/streamlit_app.py
import streamlit as st
from crew import PitchBuilder # Adjusted import
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the crew
crew = PitchBuilder().crew()

st.set_page_config(page_title="Startup Pitch Generator", layout="centered")

st.title("📝 Startup Pitch Generator")
st.write("Generate a compelling 1-page pitch for your startup's product.")

# Input form
with st.form("pitch_form"):
    topic = st.text_input("Product Topic", value="AI-Powered Health Tracker")
    submitted = st.form_submit_button("Generate Pitch")

if submitted:
    with st.spinner("Generating pitch..."):
        try:
            inputs = {"topic": topic}
            crew.kickoff(inputs=inputs)
            # Wait for a few seconds to allow pitch generation
            time.sleep(5)  # Adjust based on expected processing time

            # Fetch the generated pitch
            pitch_file = os.path.join(os.path.dirname(__file__), 'report.md')
            if os.path.exists(pitch_file):
                with open(pitch_file, 'r') as file:
                    pitch = file.read()
                st.success("📄 Pitch Generated Successfully!")
                st.markdown("### Your 1-Page Pitch")
                st.markdown(pitch)
            else:
                st.error("⚠️ Pitch file not found. Please try again.")
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
