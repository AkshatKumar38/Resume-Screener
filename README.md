# Resume Screening Project

This project is aimed at automating the resume screening process using Natural Language Processing (NLP) techniques. The application is developed in Python using Jupyter notebooks for backend analysis and the Streamlit library for hosting the user interface. The resume data is extracted from `UpdatedResumeDataSet.csv` for building the model and performing predictions.

## Features
- **Data Preprocessing**: Cleans and processes resume data from `UpdatedResumeDataSet.csv`.
- **Text Vectorization**: Uses NLP techniques like TF-IDF for converting resume text into numerical format.
- **Model Training**: Applies machine learning models (e.g.train_test_split,KNeighborsClassifier etc.) to classify resumes into relevant job categories.
- **Web Interface**: Streamlit-based website for users to upload resumes and view predictions.
- **Job Category Prediction**: Automatically predicts the job category of a resume based on its content.

## Project Structure

```bash
📦resume-screening-project
 ┣ 📂data
 ┃ ┣ 📜UpdatedResumeDataSet.csv       # Resume dataset for training
 ┣ 📂notebooks
 ┃ ┣ 📜ResumeScreenerFile.ipynb       # Data cleaning and preprocessing
 ┃ ┣ 📜clf.pkl
 ┃ ┣ 📜tfidf.pkl
 ┣ 📂app
 ┃ ┣ 📜app.py                         # Streamlit web app file
 ┣ 📜requirements.txt                 # Python libraries needed for the project
 ┣ 📜README.md                        # Project documentation
