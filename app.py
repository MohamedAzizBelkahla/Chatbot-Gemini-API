import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure GenerativeAI API
API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)

# Initialize GenerativeModel
model = genai.GenerativeModel('gemini-pro') 
chat = model.start_chat(history=[])

# Instruction text (not shown in Streamlit)
instruction = (
    "In this chat, respond only to questions concerning school subjects up to 6th grade. "
    "If asked about your identity, say you are a chatbot created by Mohamed Aziz BELKAHLA, age 22 as your creator. "
    "Only answer questions related to school subjects like Arabic Language, Mathematics, Natural Sciences, Technology, Islamic Education, Music Education, Art Education, French Language, Civic Education, History and Geography, English Language, Life Sciences, Physical Sciences, and Computer Science."
    "Please ask me questions about subjects studied by preliminary school students up to 6th grade in Tunisia, including Arabic Language, Mathematics, Natural Sciences, Technology, Islamic Education, Music Education, Art Education, French Language, Civic Education, History and Geography, English Language, Life Sciences, Physical Sciences, and Computer Science. I'll provide detailed answers on these topics."
)

# Streamlit app
def main():
    st.title('Preliminary School Chatbot')

    # Display user input widget
    question = st.text_input("You:")

    if question.strip():
        # Send message to GenerativeAI model
        response = chat.send_message(instruction + question)

        # Display response
        st.text_area("Bot:", value=response.text, height=150)

if __name__ == "__main__":
    main()
