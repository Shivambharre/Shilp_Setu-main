from src.media.imagekit import imagekit


def upload_image(file, file_name: str):


    result = imagekit.upload_file(
        file=file,
        file_name=file_name,
    )

    return {
        "url": result.url,
        "file_name": result.name,
    }


def delete_image(file_id: str):
   return imagekit.delete_file(file_id)