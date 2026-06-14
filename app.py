import streamlit as st

# Page config
st.set_page_config(page_title="My Chatbot", page_icon="🤖")

st.title("🤖 Simple Streamlit Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

def generate_response(prompt):
    """
    Simple chatbot logic (you can replace with OpenAI API later)
    """
    prompt = prompt.lower()

    if "hello" in prompt:
        return "Hi there! How can I help you today?"
    elif "name" in prompt:
        return "I am your simple Streamlit chatbot 🤖"
    elif "help" in prompt:
        return "Sure! Ask me anything and I'll try to respond."
    elif "bye" in prompt:
        return "Goodbye! Have a great day 😊"
    else:
        return "I am still learning... can you rephrase?"

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate bot response
    response = generate_response(user_input)

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display instantly
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        st.markdown(response)
