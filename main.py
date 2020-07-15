from typing import Optional 
from fastapi import FastAPI
from pydantic import BaseModel
from routing_management import FastApiRouter

app = FastAPI()


class Item(BaseModel):
    name:str
    price:float
    is_offer:Optional[bool] = None


# @app.get("/")
# def read_root():
#     return {"Hello":"World"}


#通过路由管理类来统一管理路由，来实现功能区分
fastApiRouter = FastApiRouter()
app.include_router(fastApiRouter.get_base_router())



@app.get("/items/{item_id}")
def read_item(item_id:int,q:Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/{item_id}")
def update_item(item_id:int,item:Item):
    return {"item_name": item.name, "item_id": item_id}