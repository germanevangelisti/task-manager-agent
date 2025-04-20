import axios from 'axios';

const API_URL = 'http://localhost:8000';

async function* createStreamIterator(response) {
  const reader = response.body.getReader();
  const decoder = new TextDecoder();

  try {
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      
      const chunk = decoder.decode(value, { stream: true });
      const lines = chunk.split('\n');
      
      for (const line of lines) {
        if (line.startsWith('data: ')) {
          const data = line.slice(6);
          if (data === '[DONE]') return;
          if (data.startsWith('Error:')) {
            throw new Error(data.slice(7));
          }
          yield data;
        }
      }
    }
  } finally {
    reader.releaseLock();
  }
}

export const api = {
  getTasks: () => axios.get(`${API_URL}/tasks`),
  createTask: (task) => axios.post(`${API_URL}/tasks`, task),
  updateTask: (id, task) => axios.put(`${API_URL}/tasks/${id}`, task),
  deleteTask: (id) => axios.delete(`${API_URL}/tasks/${id}`),
  
  chatWithAgent: async function* (message) {
    console.log('Sending message to chat API:', message);
    
    try {
      const response = await fetch(`${API_URL}/ai/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'text/event-stream',
        },
        body: JSON.stringify({ message }),
      });

      if (!response.ok) {
        const errorText = await response.text();
        console.error('API Error Response:', errorText);
        throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
      }

      console.log('Response received, processing stream...');
      yield* createStreamIterator(response);
      
    } catch (error) {
      console.error('Chat API error:', error);
      throw error;
    }
  }
}; 