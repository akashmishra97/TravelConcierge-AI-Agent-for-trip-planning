import streamlit as st
from advanced_travel_concierge import AdvancedTravelConcierge
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        st.title("Travel Concierge")
        st.write("Ask me anything about travel planning!")

        # User input
        user_input = st.text_input("Your question:", placeholder="e.g., Create a 3-day itinerary for Paris")

        if user_input:
            if 'concierge' not in st.session_state:
                with st.spinner("Initializing..."):
                    st.session_state.concierge = AdvancedTravelConcierge()

            with st.spinner("Thinking..."):
                response = st.session_state.concierge.get_response(user_input)
                st.write("Response:", response)

    except Exception as e:
        logger.error(f"Error: {e}")
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
