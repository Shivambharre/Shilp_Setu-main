from fastapi import FastAPI, File, UploadFile

from src.media.service import upload_image

app = FastAPI(
    title="Shilp Setu API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Shilp Setu API is running"}


@app.post("/test-image-upload")
async def test_image_upload(file: UploadFile = File(...)):
    result = upload_image(
        file=file.file,
        file_name=file.filename,
    )

    return result