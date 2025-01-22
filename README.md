# AI-phishing-Detection

<div id="chatbot">
    <div class="chat-header">Chatbot</div>
    <div class="chat-body">
        <div class="bot-message">Hello! How can I assist you today?</div>
        <div class="thinking-indicator">
            <div class="dot"></div>
            <div class="dot"></div>
            <div class="dot"></div>
        </div>
    </div>
    <div class="chat-footer">
        <input type="text" id="user-input" placeholder="Type your message..." />
        <button id="send-button">Send</button>
    </div>
</div>

#chatbot {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 300px;
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.chat-header {
    background: #5350C4;
    color: white;
    padding: 10px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
}

.chat-body {
    padding: 10px;
}

.bot-message {
    margin-bottom: 10px;
}

.thinking-indicator {
    display: flex;
}

.dot {
    width: 8px;
    height: 8px;
    margin-right: 5px;
    border-radius: 50%;
    background-color: #5350C4;
    animation: dotPulse 1.5s infinite ease-in-out;
}

@keyframes dotPulse {
    0%, 20% { transform: scale(1); }
    50% { transform: scale(1.5); }
    100% { transform: scale(1); }
}

.chat-footer {
    display: flex;
}

#user-input {
    flex-grow: 1;
}


document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    
    // Display user message
    const userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.textContent = userInput;
    
    document.querySelector('.chat-body').appendChild(userMessage);
    
    // Simulate bot response with animation
    setTimeout(() => {
        const botMessage = document.createElement('div');
        botMessage.className = 'bot-message';
        botMessage.textContent = "I'm thinking...";
        
        document.querySelector('.chat-body').appendChild(botMessage);
        
        // Show thinking indicator
        document.querySelector('.thinking-indicator').style.display = 'flex';
        
        setTimeout(() => {
            // Hide thinking indicator and show final response
            document.querySelector('.thinking-indicator').style.display = 'none';
            botMessage.textContent = "Here is my response!";
        }, 2000);
        
        // Clear input field
        document.getElementById('user-input').value = '';
        
    }, 500);
});
