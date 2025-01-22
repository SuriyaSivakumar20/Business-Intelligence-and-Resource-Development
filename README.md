# AI-phishing-Detection
# Chatbot Project

Welcome to the **Chatbot Project**! Below is a demonstration of the chatbot in action.

## Animated Chatbot

```html
<div id="chatbot-container">
  <div id="chatbot-header">
    <h3>Chatbot</h3>
  </div>
  <div id="chatbot-messages">
    <div class="message bot-message">Hello! How can I assist you today?</div>
  </div>
  <input type="text" id="user-input" placeholder="Type your message..." />
</div>

<style>
  #chatbot-container {
    width: 300px;
    height: 400px;
    border-radius: 10px;
    background-color: #f4f4f4;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    animation: fadeIn 1s ease-out;
  }

  #chatbot-header {
    background-color: #4CAF50;
    padding: 10px;
    text-align: center;
    color: white;
    font-size: 18px;
  }

  #chatbot-messages {
    flex-grow: 1;
    padding: 10px;
    overflow-y: auto;
    background-color: #fff;
    border-bottom: 2px solid #ddd;
  }

  .message {
    padding: 8px;
    margin-bottom: 5px;
    border-radius: 5px;
    font-size: 14px;
    max-width: 70%;
  }

  .bot-message {
    background-color: #e1f5fe;
    align-self: flex-start;
    animation: slideInFromLeft 0.5s ease-out;
  }

  .user-message {
    background-color: #dcedc8;
    align-self: flex-end;
    animation: slideInFromRight 0.5s ease-out;
  }

  #user-input {
    padding: 10px;
    border: none;
    border-top: 2px solid #ddd;
    font-size: 14px;
    outline: none;
  }

  #user-input:focus {
    border-color: #4CAF50;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  @keyframes slideInFromLeft {
    from {
      transform: translateX(-100%);
    }
    to {
      transform: translateX(0);
    }
  }

  @keyframes slideInFromRight {
    from {
      transform: translateX(100%);
    }
    to {
      transform: translateX(0);
    }
  }
</style>

<script>
  const userInput = document.getElementById('user-input');
  const chatbotMessages = document.getElementById('chatbot-messages');

  userInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter' && userInput.value.trim()) {
      const userMessage = document.createElement('div');
      userMessage.classList.add('message', 'user-message');
      userMessage.textContent = userInput.value;
      chatbotMessages.appendChild(userMessage);
      userInput.value = '';

      const botMessage = document.createElement('div');
      botMessage.classList.add('message', 'bot-message');
      botMessage.textContent = "I'm here to help you!";
      chatbotMessages.appendChild(botMessage);

      chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }
  });
</script>
