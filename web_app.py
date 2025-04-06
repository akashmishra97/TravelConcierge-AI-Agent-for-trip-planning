import streamlit as st
from advanced_travel_concierge import AdvancedTravelConcierge
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page config
st.set_page_config(
    page_title="Travel Concierge AI",
    page_icon="✈️",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url("https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2021&q=80");
        background-size: cover;
        background-position: center;
    }
    .title-container {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    .chat-container {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        color: white;
    }
    .user-query {
        background-color: #2c5282;
        color: white;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
    }
    .ai-response {
        background-color: #234e52;
        color: white;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
    }
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: black !important;
        border: none !important;
    }
    .stTextInput label {
        color: white !important;
    }
    .input-container {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    try:
        # Title section with custom styling
        st.markdown("""
        <div class="title-container">
            <h1>✈️ Travel Concierge AI</h1>
            <p>Your personal AI travel assistant powered by Google Gemini</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Only display chat container if there are messages
        if st.session_state.messages:
            st.markdown('<div class="chat-container">', unsafe_allow_html=True)
            # Display chat history
            for message in st.session_state.messages:
                if message["role"] == "user":
                    st.markdown(f'<div class="user-query">👤 You: {message["content"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="ai-response">🤖 AI: {message["content"]}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Input container
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        # User input
        user_input = st.text_input(
            "Ask me anything about travel planning!",
            placeholder="e.g., Create a 3-day tech-focused itinerary for San Francisco",
            key="user_input"
        )
        st.markdown('</div>', unsafe_allow_html=True)

        if user_input:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_input})

            # Initialize concierge if not exists
            if 'concierge' not in st.session_state:
                with st.spinner("Initializing AI..."):
                    st.session_state.concierge = AdvancedTravelConcierge()

            # Get AI response
            with st.spinner("Thinking..."):
                response = st.session_state.concierge.get_response(user_input)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()

    except Exception as e:
        logger.error(f"Error: {e}")
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
