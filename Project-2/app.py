import streamlit as st
import sys
import os

# Add src folder to Python's search path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from matcher import load_faqs, build_vectorizer, find_best_match


# Page configuration
st.set_page_config(page_title="E-commerce FAQ Chatbot", page_icon="🛒")

st.title("🛒 E-commerce FAQ Chatbot")
st.write("Ask me anything about orders, shipping, returns, payments, and more!")


# Load FAQs and build vectorizer ONCE, then cache it
@st.cache_resource
def setup_chatbot():
    faqs = load_faqs()
    vectorizer, faq_vectors = build_vectorizer(faqs)
    return faqs, vectorizer, faq_vectors


faqs, vectorizer, faq_vectors = setup_chatbot()

# Initialize chat history in session state (Streamlit's memory)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input box at the bottom
user_input = st.chat_input("Type your question here...")

if user_input:
    # Add user's message to chat history and display it
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Find the best matching answer
    answer, score = find_best_match(user_input, faqs, vectorizer, faq_vectors)

    # Add bot's response to chat history and display it
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)
