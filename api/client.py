import requests
import streamlit as st

def get_finance_response(input_text1):
    try:
        response = requests.post("http://localhost:8000/chat/finance/invoke", json={"input_text": input_text1})
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Finance request failed: {e}")
        return {"error": str(e)}

def get_health_response(input_text):
    try:
        response = requests.post("http://localhost:8000/chat/healthcare/invoke", json={"input_text": input_text})
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json().get('output', {}).get('content', 'No content available')
    except requests.exceptions.RequestException as e:
        print(f"Healthcare request failed: {e}")
        return {"error": str(e)}

# Streamlit framework
st.title("Langchain Demo With Groq API llama-3.3-70b-versatile")
input_text1 = st.text_input("Enter your text here related to finance")
input_text = st.text_input("Enter your text here related to healthcare")

if input_text1:
    finance_response = get_finance_response(input_text1)
    st.write(finance_response)

if input_text:
    health_response = get_health_response(input_text)
    st.write(health_response)