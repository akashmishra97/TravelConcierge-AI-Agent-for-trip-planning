# Travel Concierge AI

A smart travel concierge powered by Google's Gemini AI that helps plan trips, create itineraries, and provide travel recommendations.

## Features

- Create detailed travel itineraries
- Get destination-specific recommendations
- Modern web interface using Streamlit
- Structured day-by-day planning

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd travel-concierge-agent
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project root and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

1. Start the web interface:
```bash
streamlit run web_app.py
```

2. Open your browser and go to `http://localhost:8501`

3. Start asking questions about travel planning!

Example queries:
- "Create a 3-day tech-focused itinerary for San Francisco"
- "What are the best times to visit Tokyo?"
- "Suggest cultural activities in Paris"

## Project Structure

- `web_app.py`: Main Streamlit web interface
- `advanced_travel_concierge.py`: Core travel concierge logic
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (not included in repository)

## Technologies Used

- Python 3.8+
- Google Gemini AI
- Streamlit
- python-dotenv

## Security Note

Never commit your `.env` file or expose your API keys. The `.gitignore` file is configured to exclude sensitive information.
