# Data Visualization Dashboard
## Overview
This Streamlit dashboard provides an interactive way to visualize key insights from the cleaned datasets. The application loads pre-generated visualizations from the `plots` folder and displays them in a structured and user-friendly manner.

## Features
- **Interactive Tabs:** Easily switch between different dataset visualizations.
- **Automatic Image Detection:** Loads available images dynamically from the `plots` folder.
- **Styled Headers:** Displays the table name with an eye-catching format.
- **Full-Screen Layout:** Optimized for a responsive and immersive experience.
- **Dark/Light Mode Support:** Adapts to Streamlit's UI themes.

## Folder Structure
```
📂 Dashboard
│-- 📂 plots
│   │-- cleaned_cognito_raw.jpeg
│   │-- cleaned_cohort_data.jpeg
│   │-- cleaned_learner_oppurtunity_raw.jpeg
│   │-- cleaned_learner_raw.jpeg
│   │-- cleaned_marketing_data.jpeg
│   │-- cleaned_oppurtunity_data.png
│   │-- cleaned_opp_data.jpeg
│   │-- cleaned_opp_data_distribution.jpeg
│   │-- cleaned_user_data.png
│   │-- Top 10 countries with most learners.png
│   │--Box Plot For Outlier detection for Learner Oppurtunity Raw table.png
│   │--Histogram for Learner Oppurtunity Raw.png
│-- visualization_dashboard.py
│-- README.md
```

## Installation & Setup
### Prerequisites
Ensure you have Python installed (>=3.7) and install the required packages:
```bash
pip install streamlit pillow
```

### Running the Dashboard
Execute the following command in the terminal:
```bash
streamlit run dashboard.py
```
This will launch the interactive visualization dashboard in your default web browser.

## Usage
1. Navigate through different tabs to explore the visualizations.
2. View dataset-specific insights displayed dynamically from the `plots` folder.
3. The application will only load available images, ensuring flexibility.

## Customization
- Modify the `IMAGE_FOLDER` path in `dashboard.py` to match your image directory.
- Add new dataset visualizations in the `plots` folder to extend the dashboard.

## License
This project is licensed under the MIT License.

