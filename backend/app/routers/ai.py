from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import List, Dict
from ..database import get_db
from ..models import task as task_model
from ..schemas import task as task_schema
from ..ai.agent import TaskAIAgent
from pydantic import BaseModel

router = APIRouter(
    prefix="/ai",
    tags=["ai"]
)

class ChatMessage(BaseModel):
    message: str

class AIResponse(BaseModel):
    analysis: str | None = None
    suggestion: str | None = None
    error: str | None = None

# Inicializar el agente de IA
agent = TaskAIAgent()

def get_task_dicts(db: Session) -> List[Dict]:
    """Función auxiliar para obtener las tareas en formato diccionario"""
    tasks = db.query(task_model.Task).all()
    return [
        {
            "title": task.title,
            "description": task.description,
            "completed": task.completed
        }
        for task in tasks
    ]

async def stream_generator(generator):
    try:
        for chunk in generator:
            if chunk:  # Solo enviar si hay contenido
                yield f"data: {chunk}\n\n"
    except Exception as e:
        print(f"Error detallado en stream_generator: {str(e)}")
        import traceback
        traceback.print_exc()
        yield f"data: Error: {str(e)}\n\n"
    finally:
        yield "data: [DONE]\n\n"

@router.get("/analyze")
def analyze_tasks(db: Session = Depends(get_db)):
    try:
        task_dicts = get_task_dicts(db)
        if not task_dicts:
            return StreamingResponse(
                stream_generator(["No hay tareas para analizar."]),
                media_type="text/event-stream"
            )
        
        return StreamingResponse(
            stream_generator(agent.analyze_tasks_stream(task_dicts)),
            media_type="text/event-stream"
        )
    except Exception as e:
        print(f"Error in analyze_tasks: {str(e)}")
        return StreamingResponse(
            stream_generator(["Error al analizar las tareas."]),
            media_type="text/event-stream"
        )

@router.get("/suggest-next")
def suggest_next_task(db: Session = Depends(get_db)):
    try:
        task_dicts = get_task_dicts(db)
        if not task_dicts:
            return StreamingResponse(
                stream_generator(["No hay tareas pendientes para sugerir."]),
                media_type="text/event-stream"
            )
        
        return StreamingResponse(
            stream_generator(agent.suggest_next_task_stream(task_dicts)),
            media_type="text/event-stream"
        )
    except Exception as e:
        print(f"Error in suggest_next_task: {str(e)}")
        return StreamingResponse(
            stream_generator(["Error al generar la sugerencia."]),
            media_type="text/event-stream"
        )

@router.post("/chat")
def chat_with_agent(message: ChatMessage, db: Session = Depends(get_db)):
    try:
        task_dicts = get_task_dicts(db)
        return StreamingResponse(
            stream_generator(agent.chat_response_stream(message.message, task_dicts)),
            media_type="text/event-stream"
        )
    except Exception as e:
        print(f"Error detallado en chat_with_agent: {str(e)}")
        import traceback
        traceback.print_exc()
        return StreamingResponse(
            stream_generator([f"Error al procesar tu mensaje: {str(e)}"]),
            media_type="text/event-stream"
        ) 