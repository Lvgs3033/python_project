import google.generativeai as ai
import tkinter as tk
from tkinter import scrolledtext
import requests

# API Key
API_KEY = 'AIzaSyAcIMvSY11hx8xqBvDx7v0pqWfvxsDQu7A'

# Configure the API
ai.configure(api_key=API_KEY)

# Create a new model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# Function to handle sending a message
def send_message():
    user_message = user_input.get()
    if user_message.lower() == 'bye':
        display_text.insert(tk.END, "Chatbot: Goodbye!\n")
        root.quit()
    else:
        response = chat.send_message(user_message)
        display_text.insert(tk.END, f'You: {user_message}\n')
        display_text.insert(tk.END, f'Chatbot: {response.text}\n')
    user_input.delete(0, tk.END)

# Set up the main application window
root = tk.Tk()
root.title("Sanvad")

# Create a scrolled text widget to display the conversation
display_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20,bg='#fecfef', fg='blue')
display_text.pack(padx=10, pady=10)

# Create an entry widget for user input
user_input = tk.Entry(root, width=40)
user_input.pack(padx=10, pady=10, side=tk.LEFT)

# Create a button to send the message
send_button = tk.Button(root, text="Send", command=send_message,bg='deeppink', fg='blue')
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

# Start the GUI event loop
root.mainloop()
