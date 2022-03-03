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
