import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

os.environ["GOOGLE_API_KEY"] = "AIzaSyDCPEcdPv-N8uEH-oIVrvQdIK4zFxNRjPA"

def getGeminiresponse(input_text,no_words,blog_style,profession,language):

    model = genai.GenerativeModel('gemini-pro')

    template=f"""
        Write a creative blog in {blog_style} style for a topic {input_text}
        within {no_words} words that can help a {profession} in {language} language.
            """
    
    response = model.generate_content(template,generation_config = genai.types.GenerationConfig(temperature = 0.4))
    
    return response.text
    
    

st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Your Blog Writing Friend🤖")

input_text=st.text_input("Enter the Blog Topic")

## creating to more columns for additonal 2 fields

col1,col2,col3=st.columns([5,5,5])

professions = ['Engineer', 'Doctor', 'Teacher', 'Student','Other']

# User selection
selected_profession = st.selectbox("What's your profession:", professions,index=0)

# If 'Others' is selected, display a text input box
if selected_profession == 'Other':
        profession = st.text_input('Please type your profession:')
else:
    profession = selected_profession

with col1:
    no_words=st.text_input('No of Words')
    
with col2:
    blog_style=st.selectbox('Select the blog style',
                            ('Normal','Fun and Saracasm','Depressing','Intelligent','Motivational'),index=0)
with col3:
     language = st.selectbox('Select your output language',
                             ('English','Hindi'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getGeminiresponse(input_text,no_words,blog_style,profession,language))

st.markdown("""
    <style>
        .faded-text {
            opacity: 0.5;
        }
    </style>
    <div class="faded-text">
        Made by Gaurav Shrivastav
    </div>
""", unsafe_allow_html=True)
