import React, { useState, useEffect } from 'react';
import TaskList from './components/TaskList';
import TaskForm from './components/TaskForm';
import ChatInterface from './components/ChatInterface';
import { api } from './services/api';
import './App.css';

function App() {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const response = await api.getTasks();
      setTasks(response.data);
    } catch (error) {
      console.error('Error fetching tasks:', error);
      setError('Error al cargar las tareas');
    }
  };

  const handleCreateTask = async (task) => {
    try {
      await api.createTask(task);
      fetchTasks();
    } catch (error) {
      console.error('Error creating task:', error);
      setError('Error al crear la tarea');
    }
  };

  const handleUpdateTask = async (id, task) => {
    try {
      await api.updateTask(id, task);
      fetchTasks();
    } catch (error) {
      console.error('Error updating task:', error);
      setError('Error al actualizar la tarea');
    }
  };

  const handleDeleteTask = async (id) => {
    try {
      await api.deleteTask(id);
      fetchTasks();
    } catch (error) {
      console.error('Error deleting task:', error);
      setError('Error al eliminar la tarea');
    }
  };

  const handleChatMessage = async (message) => {
    try {
      let lastResponse = '';
      for await (const chunk of api.chatWithAgent(message)) {
        lastResponse = chunk;
      }
      return lastResponse;
    } catch (error) {
      console.error('Error in chat:', error);
      throw error;
    }
  };

  return (
    <div className="app">
      <header>
        <h1>Task Manager</h1>
        {error && <div className="error-message">{error}</div>}
      </header>
      <main>
        <div className="main-content">
          <div className="tasks-section">
            <TaskForm onSubmit={handleCreateTask} />
            <TaskList
              tasks={tasks}
              onUpdate={handleUpdateTask}
              onDelete={handleDeleteTask}
            />
          </div>
          <div className="chat-section">
            <h2>Asistente de Tareas</h2>
            <ChatInterface onSendMessage={handleChatMessage} />
          </div>
        </div>
      </main>
    </div>
  );
}

export default App; 