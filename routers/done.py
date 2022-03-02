from fastapi import APIRouter

router = APIRouter()

# TODOタスクに完了フラグを立てる
@router.put("/tasks/{task_id}/done")
async def mark_task_as_done():
  pass


# TODOタスクから完了フラグを外す
@router.delete("/tasks/{task_id}/done")
async def unmark_task_as_done():
  pass

