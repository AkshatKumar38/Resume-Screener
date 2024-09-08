import nltk #
import re # used for cleaning data
import pickle # used to seriallize and deseriallize categorical data and load data
import streamlit as st # used to make websites
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')

# loading models 
clf = pickle.load(open('clf.pkl', 'rb'))
tfidfd = pickle.load(open('tfidf.pkl','rb'))

# cleaning function
def CleanResume(txt):
    CleanedTXT = re.sub(r'http\S+\b',' ',txt)  
    CleanedTXT = re.sub(r'@\S+\b',' ',CleanedTXT)
    CleanedTXT = re.sub(r'RT|cc',' ',CleanedTXT)
    CleanedTXT = re.sub(r'#\S+',' ',CleanedTXT)
    CleanedTXT = re.sub(r'[%s]' % re.escape("""!$%^&*()_-+={}[]:;"'<,>.?/`~'"""),' ',CleanedTXT)
    CleanedTXT = re.sub(r'\s+',' ',CleanedTXT)
    return CleanedTXT  




# making website
def main():
    st.title("Resume Screening App")
    uploaded_file = st.file_uploader('Upload your resume here.', type=['text','pdf'])    
    
    if uploaded_file is not None:
        try:
            resume_byte = uploaded_file.read()
            resume_text = resume_byte.decode('utf-8')
        except UnicodeDecodeError:
            # if decoding with utf-8 fails then do it with latin-1
            resume_text = resume_byte.decode('latin-1')
        
        cleantxt = CleanResume(resume_text)
        input_feature = tfidfd.transform([cleantxt])
        prediction_id = clf.predict(input_feature)[0]
        
        
         # Map category ID to category name
        category_mapping = {
            0: "Advocate",
            1: "Arts",
            2: "Automation Testing",
            3: "Blockchain",
            4: "Business Analyst",
            5: "Civil Engineer",
            6: "Data Science",
            7: "Database",
            8: "DevOps Engineer",
            9: "DotNet Developer",
            10: "ETL Developer",
            11: "Electrical Engineering",
            12: "HR",
            13: "Hadoop",
            14: "Health and fitness",
            15: "Java Developer",
            16: "Mechanical Engineer",
            17: "Network Security Engineer",
            18: "Operations Manager",
            19: "PMO",
            20: "Python Developer",
            21: "SAP Developer",
            22: "Sales",
            23: "Testing",
            24: "Web Designing"
        }
        
        category_name = category_mapping.get(prediction_id,"Unknown")
        st.write('Prediction Category', category_name)
        
    
# python main
if __name__ == "__main__":
    main()
    