# Frontend - Task Manager UI

A React-based frontend for the Task Manager application with AI chat interface.

## Features

- Modern React UI with functional components
- Real-time task management
- AI chat interface
- Responsive design
- State management with React Hooks

## Project Structure

```
frontend/
├── src/
│   ├── components/    # React components
│   │   ├── ChatInterface.js
│   │   ├── TaskList.js
│   │   ├── TaskForm.js
│   │   └── TaskItem.js
│   ├── services/     # API services
│   │   └── api.js
│   ├── App.js        # Main component
│   └── index.js      # Entry point
├── public/           # Static files
└── package.json      # Dependencies
```

## Components

### ChatInterface
- Real-time chat with AI assistant
- Message history
- Streaming responses

### TaskList
- Display list of tasks
- Task filtering and sorting
- Task status management

### TaskForm
- Create and edit tasks
- Form validation
- Rich text input

### TaskItem
- Individual task display
- Status indicators
- Action buttons

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start development server:
   ```bash
   npm start
   ```

3. Build for production:
   ```bash
   npm run build
   ```

## Environment Variables

Create a `.env` file with the following variables:
```
REACT_APP_API_URL=http://localhost:8000
```

## Development

### Available Scripts

- `npm start` - Runs the app in development mode
- `npm test` - Launches the test runner
- `npm run build` - Builds the app for production
- `npm run eject` - Ejects from Create React App

### Code Style

- Use functional components with hooks
- Follow React best practices
- Maintain component separation
- Use meaningful variable names

### Testing

```bash
npm test
```

## API Integration

The frontend communicates with the backend through the following endpoints:

- Tasks API: `${REACT_APP_API_URL}/tasks`
- AI Chat API: `${REACT_APP_API_URL}/ai/chat`

## Contributing

1. Follow React best practices
2. Write tests for new components
3. Update documentation as needed
4. Submit a pull request

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest) 