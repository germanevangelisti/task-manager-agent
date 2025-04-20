import React, { useState, useRef, useEffect } from 'react';
import './ChatInterface.css';

const ChatInterface = ({ onSendMessage }) => {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputMessage.trim()) return;

    const userMessage = inputMessage.trim();
    setInputMessage('');
    
    // Add user message immediately
    setMessages(prev => [...prev, { text: userMessage, sender: 'user' }]);
    
    try {
      setIsTyping(true);
      // Add an empty AI message that will be updated
      setMessages(prev => [...prev, { text: '', sender: 'ai', isStreaming: true }]);
      
      const stream = await onSendMessage(userMessage);
      let accumulatedResponse = '';
      
      for await (const chunk of stream) {
        if (chunk && typeof chunk === 'string') {
          accumulatedResponse += chunk;
          // Update the last message with the accumulated response
          setMessages(prev => {
            const newMessages = [...prev];
            newMessages[newMessages.length - 1] = {
              text: accumulatedResponse,
              sender: 'ai',
              isStreaming: true
            };
            return newMessages;
          });
        }
      }
      
      // Mark the message as complete
      setMessages(prev => {
        const newMessages = [...prev];
        if (accumulatedResponse.trim()) {
          newMessages[newMessages.length - 1] = {
            text: accumulatedResponse,
            sender: 'ai',
            isStreaming: false
          };
        } else {
          // Si no hay respuesta, mostrar un mensaje de error
          newMessages[newMessages.length - 1] = {
            text: 'Lo siento, no pude generar una respuesta. Por favor, intenta de nuevo.',
            sender: 'ai',
            isError: true
          };
        }
        return newMessages;
      });
    } catch (error) {
      console.error('Chat error:', error);
      setMessages(prev => [...prev, {
        text: `Error: ${error.message || 'Hubo un error al procesar tu mensaje.'}`,
        sender: 'ai',
        isError: true
      }]);
    } finally {
      setIsTyping(false);
    }
  };

  return (
    <div className="chat-interface">
      <div className="messages-container">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`message ${message.sender} ${message.isError ? 'error' : ''}`}
          >
            <div className="message-content">
              {message.text}
              {message.isStreaming && <span className="typing-indicator">▋</span>}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <form onSubmit={handleSubmit} className="input-form">
        <input
          type="text"
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          placeholder="Escribe un mensaje..."
          disabled={isTyping}
        />
        <button type="submit" disabled={isTyping || !inputMessage.trim()}>
          {isTyping ? 'Enviando...' : 'Enviar'}
        </button>
      </form>
    </div>
  );
};

export default ChatInterface; 