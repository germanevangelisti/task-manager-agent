# Backend - Task Manager API

A FastAPI-based backend for the Task Manager application with AI integration.

## Features

- RESTful API for task management
- PostgreSQL database integration
- AI-powered task assistance using Mistral-7b-Instruct
- Real-time chat capabilities
- Docker containerization

## Project Structure

```
backend/
├── app/
│   ├── ai/           # AI integration and processing
│   ├── models/       # Database models
│   ├── routers/      # API endpoints
│   ├── schemas/      # Pydantic models
│   ├── database.py   # Database configuration
│   └── main.py       # Application entry point
├── docker-compose.yml # Docker configuration
└── requirements.txt   # Python dependencies
```

## API Endpoints

### Tasks
- `GET /tasks` - List all tasks
- `POST /tasks` - Create a new task
- `GET /tasks/{id}` - Get a specific task
- `PUT /tasks/{id}` - Update a task
- `DELETE /tasks/{id}` - Delete a task

### AI Chat
- `POST /ai/chat` - Chat with the AI assistant about tasks

## Setup

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start PostgreSQL with Docker:
   ```bash
   docker-compose up -d
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Environment Variables

Create a `.env` file with the following variables:
```
DATABASE_URL=postgresql://postgres:admin123@localhost:5432/taskmanager
LM_STUDIO_URL=http://127.0.0.1:1234/v1/chat/completions
```

## Development

### Running Tests
```bash
pytest
```

### API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Database Migrations
The application uses SQLAlchemy with automatic table creation. No additional migration steps are required.

## Docker

### Build and Run
```bash
docker-compose up -d
```

### Stop
```bash
docker-compose down
```

## Contributing

1. Follow the project's coding style
2. Write tests for new features
3. Update documentation as needed
4. Submit a pull request 