import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please add it to your .env file.")

# Configure the Gemini API
genai.configure(api_key=api_key)

# Create a model instance
model = genai.GenerativeModel(model_name)

# Make an LLM call
def make_gemini_call(prompt: str) -> str:
    """
    Makes a call to Gemini LLM with the given prompt.
    
    Args:
        prompt: The text prompt to send to Gemini
        
    Returns:
        The generated response text
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error making Gemini call: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Example prompt
    prompt = "Explain what a Large Language Model is in one paragraph."
    
    print("Sending prompt to Gemini...")
    print(f"Prompt: {prompt}\n")
    
    # Get response
    response = make_gemini_call(prompt)
    
    print("Response from Gemini:")
    print(response)
