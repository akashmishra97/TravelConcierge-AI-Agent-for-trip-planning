import os
from dotenv import load_dotenv
import google.generativeai as genai
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

class AdvancedTravelConcierge:
    def __init__(self):
        try:
            # Using gemini-1.5-pro-latest model
            model_name = 'gemini-1.5-pro-latest'
            logger.info(f"Initializing model: {model_name}")
            self.model = genai.GenerativeModel(model_name)
            
            # Test the model
            test_response = self.model.generate_content("Hello")
            logger.info("Model test successful")
            
        except Exception as e:
            logger.error(f"Error initializing model: {e}")
            raise
    
    def get_response(self, query):
        try:
            # Add travel context to the query
            prompt = f"""As a travel concierge, help with this query: {query}
            If this is an itinerary request, format the response as:
            Day 1:
            - Morning: [activity]
            - Afternoon: [activity]
            - Evening: [activity]
            
            Day 2:
            - Morning: [activity]
            - Afternoon: [activity]
            - Evening: [activity]
            
            For tech-focused itineraries, include visits to tech companies, innovation centers, and tech museums.
            Provide helpful, accurate, and concise travel advice."""
            
            logger.info("Generating response...")
            response = self.model.generate_content(prompt)
            logger.info("Response generated successfully")
            return response.text
            
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            raise

if __name__ == "__main__":
    # Test the concierge
    concierge = AdvancedTravelConcierge()
    response = concierge.get_response("Tell me about Paris")
    print(response)
