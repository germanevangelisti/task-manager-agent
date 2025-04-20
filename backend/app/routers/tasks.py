from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import task as task_model
from ..schemas import task as task_schema

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.get("/", response_model=List[task_schema.Task])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(task_model.Task).all()
    return tasks

@router.post("/", response_model=task_schema.Task)
def create_task(task: task_schema.TaskCreate, db: Session = Depends(get_db)):
    db_task = task_model.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/{task_id}", response_model=task_schema.Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=task_schema.Task)
def update_task(task_id: int, task: task_schema.TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    for key, value in task.dict().items():
        setattr(db_task, key, value)
    
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"} 