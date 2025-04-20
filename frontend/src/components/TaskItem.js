import React from 'react';

const TaskItem = ({ task, onToggle, onDelete }) => {
  return (
    <div className={`task-item ${task.completed ? 'completed' : ''}`}>
      <input
        type="checkbox"
        checked={task.completed}
        onChange={() => onToggle(task.id)}
      />
      <div className="task-content">
        <h3>{task.title}</h3>
        <p>{task.description}</p>
      </div>
      <button onClick={() => onDelete(task.id)} className="delete-btn">
        Delete
      </button>
    </div>
  );
};

export default TaskItem; 