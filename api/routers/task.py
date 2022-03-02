from  fastapi import APIRouter

router = APIRouter()

# TODOリストを表示する
@router.get("/tasks")
async def list_tasks():
  pass

# TODOにタスクを追加する
@router.post("/tasks")
async def create_task():
  pass


# TODOにタスクの説明文を変更する
@router.put("/tasks/{task_id}")
async def update_task():
  pass


# TODOのタスク自体を削除する
@router.delete("/tasks/{task_id}")
async def ddelete_task():
  pass

