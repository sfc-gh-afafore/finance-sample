import streamlit as st
from transformers import pipeline

def main():
    st.title("Interactive LLM Data Explorer")

    # Get user input
    user_input = st.text_input("Enter your text:")

    # Generate response using LLM
    if user_input:
        response = generate_response(user_input)
        st.write("### LLM Response:")
        st.write(response)


def generate_response(input_text):
    """
    Function to generate response using a pre-trained LLM.
    """
    # Load pre-trained model
    text_generator = pipeline("text-generation", model="gpt2")

    # Generate response
    response = text_generator(input_text, max_length=50, do_sample=False)
    return response[0]['generated_text']


if __name__ == "__main__":
    main()
