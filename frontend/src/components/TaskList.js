import React from 'react';
import TaskItem from './TaskItem';

const TaskList = ({ tasks, onUpdate, onDelete }) => {
  return (
    <div className="task-list">
      {tasks.map((task) => (
        <TaskItem
          key={task.id}
          task={task}
          onToggle={() => onUpdate(task.id, { ...task, completed: !task.completed })}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
};

export default TaskList; 