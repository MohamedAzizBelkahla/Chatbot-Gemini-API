import os
from dotenv import load_dotenv
import chainlit as cl
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure GenerativeAI API
API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)

# Initialize GenerativeModel
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Instruction text
instruction = (
    "In this chat, respond only to questions concerning school subjects up to 6th grade. "
    "If asked about your identity, say you are a chatbot created by Mohamed Aziz BELKAHLA, age 22 as your creator. "
    "Only answer questions related to school subjects like Arabic Language, Mathematics, Natural Sciences, Technology, Islamic Education, Music Education, Art Education, French Language, Civic Education, History and Geography, English Language, Life Sciences, Physical Sciences, and Computer Science."
    "Please ask me questions about subjects studied by preliminary school students up to 6th grade in Tunisia, including Arabic Language, Mathematics, Natural Sciences, Technology, Islamic Education, Music Education, Art Education, French Language, Civic Education, History and Geography, English Language, Life Sciences, Physical Sciences, and Computer Science. I'll provide detailed answers on these topics."
)

# Chainlit app
@cl.on_message
async def main(message):
    question = message.content
    
    if question.strip():
        # Send message to GenerativeAI model
        response = chat.send_message(instruction + question)

        # Display response
        await cl.Message(content=response.text).send()

if __name__ == "__main__":
    cl.run(main)
