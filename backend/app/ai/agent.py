import requests
from typing import List, Dict, Generator
import os
import json

class TaskAIAgent:
    def __init__(self):
        self.api_url = os.getenv("LM_STUDIO_URL", "http://127.0.0.1:1234/v1/chat/completions")
        self.model = "mistral-7b-instruct-v0.2"

    def _format_tasks(self, tasks: List[Dict]) -> str:
        if not tasks:
            return "No hay tareas registradas."

        pending = [t for t in tasks if not t['completed']]
        completed = [t for t in tasks if t['completed']]
        
        result = []
        
        if pending:
            result.append("Tareas pendientes:")
            for task in pending:
                result.append(f"• {task['title']}")
                if task.get('description'):
                    result.append(f"  → {task['description']}")
        
        if completed:
            if result:
                result.append("")
            result.append("Tareas completadas:")
            for task in completed:
                result.append(f"✓ {task['title']}")
        
        return "\n".join(result)

    def chat_response_stream(self, message: str, tasks: List[Dict]) -> Generator[str, None, None]:
        try:
            task_info = self._format_tasks(tasks)
            print(task_info)
            
            # Formato específico para Mistral-7b-Instruct
            conversation = [
                {"role": "user", "content": "Eres un asistente de tareas en español. Debes responder de manera clara y directa."},
                {"role": "assistant", "content": "Entendido. Estoy listo para ayudarte con la gestión de tus tareas. ¿En qué puedo ayudarte?"},
                {"role": "user", "content": f"""Estado actual de tareas:
{task_info}

Consulta del usuario: {message}

Por favor, responde considerando lo siguiente:
- Sé específico sobre las tareas mencionadas
- Si preguntan por tareas pendientes, enuméralas
- Si no hay tareas relevantes, indícalo claramente"""}
            ]

            response = requests.post(
                self.api_url,
                json={
                    "messages": conversation,
                    "model": self.model,
                    "temperature": 0.3,
                    "top_p": 0.5,
                    "max_tokens": 250,
                    "stream": False
                },
                stream=False,
                timeout=40
            )
            response.raise_for_status()
            
            # Procesar la respuesta
            response_data = response.json()
            
            if response_data.get('choices') and len(response_data['choices']) > 0:
                content = response_data['choices'][0].get('message', {}).get('content', '')
                if content:
                    yield content
                else:
                    yield "No se pudo obtener una respuesta clara del modelo."
            else:
                yield "No se recibió una respuesta válida del modelo."

        except Exception as e:
            print(f"Error en chat: {e}")
            yield "Lo siento, hubo un error al procesar tu consulta. Por favor, intenta nuevamente." 