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

## Environment Configuration

Before running the application, you need to set up your environment variables. Create a `.env` file in the `backend` directory with the following structure:

```env
# Database Configuration
POSTGRES_USER=your_postgres_username
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=taskmanager
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Database URL (used by SQLAlchemy)
DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

# AI Configuration
LM_STUDIO_URL=http://127.0.0.1:1234/v1/chat/completions

# Application Configuration
APP_HOST=0.0.0.0
APP_PORT=8000
DEBUG=True

# Security
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Make sure to:
1. Replace `your_postgres_username` and `your_postgres_password` with your actual PostgreSQL credentials
2. Set a secure `SECRET_KEY` for JWT token generation
3. Adjust the `LM_STUDIO_URL` if your LM Studio server runs on a different port

## Getting Started

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd task-manager-interview
   ```

2. Set up environment variables as described above

3. Start the backend:
   ```bash
   cd backend
   docker-compose up -d
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

4. Start the frontend:
   ```bash
   cd frontend
   npm install
   npm start
   ```

5. Start LM Studio:
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