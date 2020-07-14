1.安装python：我用的时miniconda同意管理
2.安装虚拟环境：pip3 install virtualenv
3.创建虚拟环境：virtualenv fast
4.启动虚拟环境：source fast/bin/activate (退出时deactivate)
5.安装包： pip3 install -r env.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple
6.启动项目：uvicorn main:app --reload
7.启动之后接口管理：http://127.0.0.1:8000/docs
8.官方文档：https://fastapi.tiangolo.com/zh/