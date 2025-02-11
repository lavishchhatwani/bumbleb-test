from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import List
from todo_app import setting

app = FastAPI()

class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str = Field(index=True, min_length=3, max_length=54)
    is_complete: bool = Field(default=False)

connection_string = str(setting.DATABASE_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, connect_args={"sslmode": "require"}, pool_recycle=300, pool_size=10)

# Create database tables
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

@app.post("/todo/", response_model=Todo)
async def create_todo(todo: Todo, session: Session = Depends(get_session)):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@app.get("/todo/", response_model=List[Todo])
async def read_todos(session: Session = Depends(get_session)):
    todos = session.exec(select(Todo)).all()
    return todos

@app.get("/todo/{todo_id}", response_model=Todo)
async def read_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todo/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo_data: Todo, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.content = todo_data.content
    todo.is_complete = todo_data.is_complete
    session.commit()
    session.refresh(todo)
    return todo

@app.delete("/todo/{todo_id}", response_model=dict)
async def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(todo)
    session.commit()
    return {"message": "Todo deleted successfully"}
