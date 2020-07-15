#引入必要的组件
from fastapi import APIRouter, HTTPException, Request, status

def get_base_router()->APIRouter:
    router = APIRouter()
    @router.get("/")
    def read_root(request: Request):
        return {"Hello":"World"}
    return router
