import gradio as gr
import random
import time

# First screenshot: Create a simple chatbot interface using Gradio
"""
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    # Define the response function
    def respond(message, chat_history):
        # Simulate a random chatbot response
        bot_message = random.choice(["Keep pushing!", "Take 3 deep breaths :)", "When did you last eat/ drink?."])
        # Update chat history
        chat_history.append(
            {
                "role": "user",
                "content": message
            }
        )
        # Append bot response
        chat_history.append(
            {
                "role": "assistant",
                "content": bot_message
            }
        )
        # Simulate a delay for response
        time.sleep(1)  
        # Return updated chat history
        return "", chat_history
    # Bind the submit event to the respond function
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
"""

# Second screenshot: Simple chatbot with nice typing effect & immediate user response
"""
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton()

    # Define the user function to update chat history
    def user(user_message, history: list):
        return "", history + [{
            "role": "user",
            "content": user_message
        }]
    
    def bot(history: list):
        bot_message = random.choice(["How old are you?", "What is your favorite color?", "What is the airspeed velocity of an unladen swallow?"])
        history.append({
            "role": "assistant",
            "content": ""
        })
        # Simulate typing effect
        for char in bot_message:
            history[-1]['content'] += char
            time.sleep(0.05)
            yield history # Update the chat history incrementally

    # Bind the submit event to the user and bot functions (the queue=False for immediate response)
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then( 
        bot, chatbot, chatbot
    )
"""

# demo.launch()


