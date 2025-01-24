# Zeynep Caysar Bachelor Thesis  
**Title:** Exploratory Data Analysis and Predictive Modeling of Migraine Attacks and Quality of Life: Using Physical Activity, Sleep, and Stress Patterns  

This project focuses on exploring the relationships between physical activity, sleep, and stress patterns and their impact on migraine occurrence, severity, and quality of life. The repository is structured into several folders and files for preprocessing, analysis, modeling, and creating a dashboard.  

---

## Project Directory Structure  

### `src` Folder  
Contains all the code files and subfolders necessary for the project:  

- **`descriptive_analysis` folder**  
  - `long_dataset_descriptives.ipynb`: Descriptive analysis for the long dataset.  
  - `short_dataset_descriptives.ipynb`: Descriptive analysis for the short dataset.  

- **`feature_engineering` folder**  
  - `long_dataset_feature_engineering.ipynb`: Feature engineering for the long dataset.  
  - `short_dataset_feature_engineering.ipynb`: Feature engineering for the short dataset.  

- **`predictive_modeling` folder**  
  - Subfolders for predictive modeling tasks:  
    - **`long_dataset_models`**: Models for the long dataset.  
    - **`short_dataset_models`**: Models for the short dataset.  
    - Predictive tasks include:
      - Migraine frequency  
      - Migraine duration  
      - Pain intensity  
      - Next migraine occurrence (next 7 days)  
      - Affected quality of life (QoL)  
      - Next migraine occurrence (next day - short dataset only)  
      - Severe migraine prediction (long dataset only)  

- **`preprocessing_datasets` folder**  
  - `long_dataset_preprocess.ipynb`: Preprocessing for the long dataset.  
  - `short_dataset_preprocess.ipynb`: Preprocessing for the short dataset.  

- **`statistical_analysis` folder**  
  - `long_dataset_stats.ipynb`: Statistical analysis (correlations, tests) for the long dataset.  
  - `short_dataset_stats.ipynb`: Statistical analysis for the short dataset.  

- **`templates` folder**  
  - `index.html`: Main page of the web app.  
  - `result.html`: Results page of the web app.  

- **`static` folder**  
  - `styles.css`: CSS file for styling the web app.  
  - `images/`: Directory for storing images.  

- **`app.py`**  
  - Python script for running the pain intensity prediction dashboard.  

---

## How to Run the Project  

### Prerequisites  
1. Install Python 3.8+ on your system.  
2. Install the required Python packages written in requirements.txt file.

### Step-by-Step Instructions

1. **Preprocessing the Datasets**
   - Navigate to the `preprocessing_datasets` folder.
   - Run the following files with the long and short MBuddy datasets to generate filtered datasets:
     - `long_dataset_preprocess.ipynb` → Outputs `final_minimum_migraine_sleep.csv`.
     - `short_dataset_preprocess.ipynb` → Outputs `final_minimum_migraine.csv`.

2. **Feature Engineering**
   - Navigate to the `feature_engineering` folder.
   - Run the following files with the preprocessed datasets:
     - `long_dataset_feature_engineering.ipynb` → Outputs `final_long.csv`.
     - `short_dataset_feature_engineering.ipynb` → Outputs `final_short.csv`.

3. **Descriptive Analysis**
   - Navigate to the `descriptive_analysis` folder.
   - Run the respective notebooks:
     - `long_dataset_descriptives.ipynb` (for `final_long.csv`)
     - `short_dataset_descriptives.ipynb` (for `final_short.csv`)

4. **Statistical Analysis**
   - Navigate to the `statistical_analysis` folder.
   - Run the respective notebooks:
     - `long_dataset_stats.ipynb` (for `final_long.csv`)
     - `short_dataset_stats.ipynb` (for `final_short.csv`)

5. **Predictive Modeling**
   - Navigate to the `predictive_modeling` folder.
   - Run the models in the respective subfolders:
     - `long_dataset_models` (for `final_long.csv`)
     - `short_dataset_models` (for `final_short.csv`)

6. **Dashboard**
   - Ensure that the `gb_model_short_dataset_pain_intensity.pkl` file exists in the specified path.
   - Run the `app.py` file.
   - Open your browser and visit: [http://127.0.0.1:5001/](http://127.0.0.1:5001/).


