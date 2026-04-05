from ollama import chat, ChatResponse

# 1. MEMÓRIA INICIAL: Definimos a 'regra do jogo' (system)
history = [
    {
        'role': 'system', 
        'content': 'Você é um assistente pessoal. Responda de forma curta, clara e use apenas um emoji por resposta.'
    }
]

while True:
    # 2. ENTRADA: Capturamos a fala do usuário
    user_input = input("Você: ") 
    
    # 3. REGISTRO (User): Guardamos o que o usuário disse no histórico
    history.append({'role': 'user', 'content': user_input}) 
    
    # 4. PROCESSAMENTO: Enviamos a lista COMPLETA para o modelo
    # 'messages=history' garante que a IA leia o passado antes de responder
    response: ChatResponse = chat(model='llama3.2:1b', messages=history)
    
    # 5. SAÍDA: Exibimos apenas o texto da resposta (.content)
    print(f"IA: {response.message.content}") 
    
    # 6. REGISTRO (AI): 'Grampeamos' a resposta da IA no histórico 
    # Isso evita que ela esqueça o que acabou de dizer na próxima rodada
    history.append(response.message)