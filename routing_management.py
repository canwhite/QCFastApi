#用来管理路由
from fastapi import APIRouter, Request
from router import get_base_router

class FastApiRouter:
    def __init__(self):
        print('init')

    def get_base_router(self)->APIRouter:
        return get_base_router()