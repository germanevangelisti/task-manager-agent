# Task Manager with AI Assistant

A modern task management application with an integrated AI assistant powered by Mistral-7b-Instruct. This project demonstrates a full-stack application with a Python FastAPI backend and a React frontend.

## Features

- Task management (create, read, update, delete)
- AI-powered task assistance
- Real-time chat interface
- PostgreSQL database
- Docker containerization

## Project Structure

```
task-manager-interview/
├── backend/          # FastAPI backend
├── frontend/         # React frontend
└── README.md         # This file
```

## Prerequisites

- Python 3.8+
- Node.js 14+
- Docker and Docker Compose
- LM Studio (for local AI model)

## Getting Started

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd task-manager-interview
   ```

2. Start the backend:
   ```bash
   cd backend
   docker-compose up -d
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

3. Start the frontend:
   ```bash
   cd frontend
   npm install
   npm start
   ```

4. Start LM Studio:
   - Download and install LM Studio
   - Load the Mistral-7b-Instruct model
   - Start the local server

## Documentation

- [Backend Documentation](./backend/README.md)
- [Frontend Documentation](./frontend/README.md)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 