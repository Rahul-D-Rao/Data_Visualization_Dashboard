import streamlit as st
import os
from PIL import Image

# Set Streamlit page configuration
st.set_page_config(page_title="Data Visualization Dashboard", layout="wide")

# Title and Description
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 Data Visualization Dashboard</h1>", unsafe_allow_html=True)
st.write("Explore the key insights from the cleaned datasets through interactive visualizations.")

# Path to the plots folder
IMAGE_FOLDER = "plots/"

# Dictionary mapping filenames to human-readable table names
image_mapping = {
    "cleaned_cognito_raw.jpeg": "Cognito Raw",
    "cleaned_cohort_data.jpeg": "Cohort Data",
    "cleaned_learner_oppurtunity_raw.jpeg": "Learner Opportunity Raw",
    "cleaned_learner_raw.jpeg": "Learner Raw",
    "cleaned_marketing_data.jpeg": "Marketing Data",
    "cleaned_oppurtunity_data.png": "Opportunity Data",
    "cleaned_opp_data.jpeg": "Opp Data",
    "cleaned_opp_data_distribution.jpeg": "Opp Data Distribution",
    "cleaned_user_data.png": "User Data",
    "Top 10 countries with most learners.png": "Top 10 Countries with Most Learners",
    "Box Plot For Outlier detection for Learner Oppurtunity Raw table.png": "Box Plot for Outlier Detection (Learner Opportunity Raw)",
    "Histogram for Learner Oppurtunity Raw.png": "Histogram for Learner Opportunity Raw"
}

# Filter only available images in the folder
available_images = {file: name for file, name in image_mapping.items() if file in os.listdir(IMAGE_FOLDER)}

# Sidebar for navigation
st.sidebar.title("📌 Select a Dataset Visualization")
selected_plot = st.sidebar.radio("Choose a dataset:", list(available_images.values()))

# Display selected image
if selected_plot:
    file_name = [key for key, val in available_images.items() if val == selected_plot][0]
    img_path = os.path.join(IMAGE_FOLDER, file_name)

    # Load and display the image
    image = Image.open(img_path)
    st.markdown(f"<h2 style='text-align: center; color: #2196F3;'>📌 {selected_plot}</h2>", unsafe_allow_html=True)
    st.image(image, caption=f"{selected_plot} Visualization", use_container_width=True)
else:
    st.error("❌ No visualization images found. Please check the 'plots' folder.")
