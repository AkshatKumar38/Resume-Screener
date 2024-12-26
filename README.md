# Resume Screener

The Resume Screener is a machine learning-based application designed to automate the process of filtering and ranking resumes. It leverages natural language processing (NLP) and classification models to identify the most suitable candidates based on predefined criteria.

## Project Structure

- **`App/`**: Contains the application code for running the Resume Screener.  
- **`clf.pkl`**: Pre-trained classification model used to predict candidate suitability.  
- **`Data/`**: Stores datasets used for training, validation, or testing.  
- **`Notebooks/`**: Jupyter notebooks for data analysis, feature engineering, or model development.  
- **`requirements.txt`**: Specifies the Python dependencies required to run the project.  
- **`tfidf.pkl`**: Pre-trained TF-IDF vectorizer for text feature extraction.

## Features

- **Resume Parsing**: Extracts key information such as skills, experience, and education.  
- **TF-IDF Vectorization**: Converts resume text into a machine-readable format.  
- **Classification**: Uses a pre-trained model (`clf.pkl`) to rank resumes based on relevance.  
- **Scalability**: Processes multiple resumes simultaneously.  

## Requirements

To set up and run the project, install the required dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```
## Installation and Setup
1. Clone the repository:
```bash
Copy code
git clone https://github.com/AkshatKumar38/Resume-Screener.git
```
2. Navigate to the project directory:
```bash
Copy code
cd Resume-Screener
```
3. Install the required Python libraries:
```bash
Copy code
pip install -r requirements.txt
```
## Usage
- Run the main application located in the App/ directory.
- Provide a dataset or upload resumes in the supported formats.
- View the processed results, which include rankings and insights.

## Technical Overview
- Machine Learning: The classifier (clf.pkl) predicts the suitability of resumes based on pre-defined labels.
- Text Processing: TF-IDF (tfidf.pkl) transforms textual data into meaningful numerical features.
- Interactive Analysis: Jupyter notebooks in Notebooks/ offer detailed exploratory and feature engineering workflows.

## License
This project is licensed under the MIT License.

## Contact
For further inquiries or feedback, feel free to contact: Akshat Kumar
GitHub: AkshatKumar38
