from fastapi import FastAPI, File, UploadFile

import task
from src.media.service import upload_image

from src.user.router import user_routes
from src.task.router import task_routes

app = FastAPI(
    title="Shilp Setu API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Shilp Setu API is running"}


@app.post("/test_upload")
async def test_image_upload(file: UploadFile = File(...)):
    result = upload_image(
        file=file.file,
        file_name=file.filename,
    )

    return result
app.include_router(user_routes)
app.include_router(task_routes)