from ollama import chat, ChatResponse

# 1. INITIAL MEMORY: Defining the 'rules of the game' (System Prompt)
history = [
    {
        'role': 'system', 
        'content': 'You are a personal assistant. Keep your answers short, clear, and use only one emoji per response.'
    }
]

while True:
    # 2. INPUT: Capture user input from the terminal
    user_input = input("You: ") 
    
    # 3. REGISTRATION (User): Save user's message to the chat history
    history.append({'role': 'user', 'content': user_input}) 
    
    # 4. PROCESSING: Send the ENTIRE history to the model
    # 'messages=history' ensures the AI considers previous context before responding
    response: ChatResponse = chat(model='llama3.2:1b', messages=history)
    
    # 5. OUTPUT: Display only the text content of the response
    print(f"AI: {response.message.content}") 
    
    # 6. REGISTRATION (AI): Append the AI's response to the history
    # This prevents the model from forgetting what it just said in the next turn
    history.append(response.message)