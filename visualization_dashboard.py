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
    "cleaned_user_data.png": "User Data"
}

# Filter only the available images in the folder
available_images = {file: name for file, name in image_mapping.items() if file in os.listdir(IMAGE_FOLDER)}

# Create tabs for each dataset visualization
if available_images:
    tabs = st.tabs(list(available_images.values()))

    for index, (file_name, table_name) in enumerate(available_images.items()):
        with tabs[index]:  # Assign each plot to its respective tab
            img_path = os.path.join(IMAGE_FOLDER, file_name)
            image = Image.open(img_path)
            
            # Display image with a formatted title
            st.markdown(f"<h2 style='text-align: center; color: #2196F3;'>📌 {table_name}</h2>", unsafe_allow_html=True)
            st.image(image, caption=f"{table_name} Visualization", use_container_width=True)
else:
    st.error("❌ No visualization images found. Please check the 'plots' folder.")
