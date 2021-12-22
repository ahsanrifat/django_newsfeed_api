from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from moviepy.editor import *


def PIL_image_to_django_file(img, filename):
    thumb_io = BytesIO()
    img.save(thumb_io, format="png")
    photo = ContentFile(thumb_io.getvalue(), f"{filename}.png")
    return photo


def generate_thumbnail_from_video_file(movie_py_video_object):
    frame_data = movie_py_video_object.get_frame(1)
    img = Image.fromarray(frame_data, "RGB")
    return img
