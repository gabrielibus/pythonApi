# FIRST INSTALL
# pip install fastapi
# pip install pillow
# DEPLOY: https://ckwebstudio.com/posts/host-python-fast-api-app-in-cloud-vps-with-ubuntu-20-04-gunicorn-and-caddy2-web-server

from fastapi import FastAPI
from fastapi.responses import FileResponse
from addTextToImage import generateImg

app = FastAPI()


@app.get("/")
def main():
    return {"Estoy melo!"}


# @app.get("/get_image")
# async def main(text, position, salary, working_time, template):
#     imageFile = generateImg(text=text, position=position, salary=salary,
#                             workingTime=working_time, template=template)
#     return FileResponse(imageFile)
