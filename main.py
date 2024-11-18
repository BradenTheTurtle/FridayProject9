import tkinter as tk
from tkinter import messagebox
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from .env
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please ensure your .env file is configured correctly.")

# Set OpenAI API key
openai.api_key = api_key

# Function to generate a response using GPT-4
def generate_response():
    user_input = text_input.get("1.0", tk.END).strip()  # Get the text input from the user
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a prompt!")
        return

    try:
        # Prepare the messages for chat-based API (using role "user" for the prompt)
        messages = [
            {"role": "user", "content": user_input}
        ]
        
        # Make the API call to OpenAI for GPT-4 using the ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use gpt-4 model
            messages=messages,  # Provide the conversation context
            max_tokens=100,  # Adjust the number of tokens as needed
            temperature=0.7,  # Adjust creativity (0.0 to 1.0)
        )

        # Extract the assistant's response and display it in the output box
        text_output.delete("1.0", tk.END)  # Clear previous output
        text_output.insert(tk.END, response.choices[0].message['content'].strip())  # Display response
    
    except Exception as e:
        messagebox.showerror("API Error", f"An error occurred: {str(e)}")

# Create the main window (root)
root = tk.Tk()
root.title("OpenAI GPT-4 Text Generator")

# Set window size
root.geometry("600x400")

# Instructions Label
instructions_label = tk.Label(root, text="Enter your prompt below and click Submit.", font=("Arial", 14))
instructions_label.pack(pady=10)

# Text Input Box for user to type prompt
text_input = tk.Text(root, height=5, wrap=tk.WORD, font=("Arial", 12))
text_input.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Submit Button to generate response
submit_button = tk.Button(root, text="Submit", command=generate_response, font=("Arial", 14), bg="blue", fg="white")
submit_button.pack(pady=10)

# Output Box to display API response
text_output = tk.Text(root, height=10, wrap=tk.WORD, font=("Arial", 12), bg="lightgray")
text_output.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
root.mainloop()
