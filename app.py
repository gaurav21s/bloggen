import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To get response from LLAma 2 model
os.environ["GOOGLE_API_KEY"] = "AIzaSyDCPEcdPv-N8uEH-oIVrvQdIK4zFxNRjPA"

def getGeminiresponse(input_text,no_words,blog_style):

    model = genai.GenerativeModel('gemini-pro')

    template=f"""
        Write a creative blog in {blog_style} style for a topic {input_text}
        within {no_words} words.
            """
    
    response = model.generate_content(template,generation_config = genai.types.GenerationConfig(temperature = 0.3))
    
    return response.text
    
    

st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the Blog Topic")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Fun and Saracastic','Depressing','Normal','Intelligent'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getGeminiresponse(input_text,no_words,blog_style))
