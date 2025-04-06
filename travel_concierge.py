import os
from dotenv import load_dotenv
import google.generativeai as genai
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.memory.dict_memory import DictMemory
from agno.knowledge.text import TextKnowledgeBase
from agno.vectordb.memory import MemoryVectorDb

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Travel tips knowledge base content
travel_tips = """
Travel Tips:
1. Always carry a photocopy of your passport and important documents.
2. Notify your bank before traveling internationally to avoid card blocks.
3. Pack a basic first-aid kit with essential medications.
4. Learn a few basic phrases in the local language.
5. Research local customs and etiquette before your trip.
6. Use a money belt or hidden pouch in crowded tourist areas.
7. Keep digital copies of all important documents in cloud storage.
8. Check if your phone plan includes international coverage.
9. Bring a universal power adapter for international travel.
10. Register with your country's embassy when traveling to high-risk areas.
"""

def create_travel_agent():
    # Create a vector database for our knowledge base
    vector_db = MemoryVectorDb()
    
    # Create a knowledge base with travel tips
    knowledge = TextKnowledgeBase(
        text=travel_tips,
        vector_db=vector_db
    )
    
    # Create memory for the agent to remember conversation history
    memory = DictMemory()
    
    # Create the Gemini model
    model = genai.GenerativeModel('gemini-pro')
    
    # Create the agent with tools, knowledge, and memory
    agent = Agent(
        model=model,
        description="You are a helpful Travel Concierge that assists users in planning their trips.",
        instructions=[
            "Help users plan their trips by providing destination information, travel tips, and itineraries.",
            "Use web search to find up-to-date information about destinations.",
            "Remember user preferences and trip details for follow-up questions.",
            "Access your knowledge base for general travel tips and advice.",
            "Always be friendly, enthusiastic, and helpful."
        ],
        tools=[
            DuckDuckGoTools(),  # For web search
        ],
        knowledge=knowledge,     # Travel tips knowledge base
        memory=memory,          # To remember conversation history
        show_tool_calls=True,   # Show when tools are being used
        markdown=True           # Format responses in markdown
    )
    
    return agent

def chat_with_agent(query):
    """Function to interact with the agent and print the response"""
    response = travel_agent.get_response(query)
    print("\nUser: " + query)
    print("\nTravel Concierge: " + response)
    return response

# Create and initialize the agent
travel_agent = create_travel_agent()

if __name__ == "__main__":
    print("Travel Concierge Agent initialized! Ask about planning a trip.")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Thank you for using the Travel Concierge Agent. Happy travels!")
            break
        
        chat_with_agent(user_input)
