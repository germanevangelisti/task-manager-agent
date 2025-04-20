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
├── .env              # Environment variables (not in git)
└── requirements.txt   # Python dependencies
```

## Environment Configuration

The application requires a `.env` file in the root of the backend directory. Create this file with the following structure:

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

### Important Notes:
1. The `.env` file is not tracked by git for security reasons
2. You must create this file manually before running the application
3. Replace the placeholder values with your actual configuration
4. The `DATABASE_URL` is automatically constructed from the individual PostgreSQL variables

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

3. Create and configure the `.env` file as described above

4. Start PostgreSQL with Docker:
   ```bash
   docker-compose up -d
   ```

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
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