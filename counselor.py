import google.generativeai as genai
import os

# Configuration
API_KEY = "YOUR_API_KEY"
genai.configure(api_key=API_KEY)

# Define the Professional Counselor Persona
SYSTEM_PROMPT = (
    "You are a professional counselor. Your tone is empathetic, patient, "
    "and non-judgmental. You use active listening techniques, reflect "
    "feelings, and ask open-ended questions. You provide a safe space "
    "for professional and personal growth while maintaining clear boundaries."
)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)

def start_counseling_session():
    chat_session = model.start_chat(history=[])
    
    print("-" * 50)
    print("Gemini Counselor: Hello. I am here to listen. What is on your mind?")
    print("(Type 'quit' to end the session)")
    print("-" * 50)

    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("\nCounselor: Take care of yourself. Goodbye.")
            break

        try:
            response = chat_session.send_message(user_input)
            print(f"\nCounselor: {response.text}\n")
        except Exception as e:
            print(f"\n[Error]: {e}")

if __name__ == "__main__":
    start_counseling_session()
