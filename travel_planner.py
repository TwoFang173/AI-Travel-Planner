import openai
import json

# Load API key from OpenAI
API_KEY = "YOUR_OPENAI_API_KEY"
client = OpenAI(api_key=API_KEY)

# Unstructed class note
travel_request = input("Where and for how long do you want to travel? (e.g., a 5-day trip to Paris for a history buff): ")

# The prompt for a simple JSON object with two keys
# The detailed system prompt for our final application
system_prompt = """
You are an expert travel planner. Your task is to take the provided travel request and generate a structured travel plan.
You must format your output as a single JSON object with the following keys:
- "destination": A string with the travel destination.
- "duration_days": A string with the duration of the trip (as a number).
- "detailed_itinerary": A list of JSON objects, where each object has three keys:
    - "day": The day number (e.g., "Day 1").
    - "focus": A short theme for the day (e.g., "Historical Deep Dive").
    - "activities": a list of 2-3 specific activity strings for that day.
"""

try:
    response = client.responses.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": travel_request}
        ],
        response_format={"type": "json_object"}
    )
    
    # Extract the JSON string from the response
    study_guide = json.loads(response.output_text)

    # --- Print the formatted study guide ---
    print("--- AI-Generated Travel Plan ---")

    print(f"\nDestination: {study_guide['destination']}")
    print(f"Duration: {study_guide['duration_days']} days")

    print("\n✅ Daily Plan:")
    for item in study_guide["detailed_itinerary"]:
        print(f"- {item['day']}: {item['focus']} - {item['activities']}")
        for activity in item['activities']:
            print(f"   • {activity}")
except Exception as e:
    print(f"An error occurred: {e}")