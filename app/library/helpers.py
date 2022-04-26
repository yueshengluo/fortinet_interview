import os.path
import uuid
from pathlib import Path
from PIL import Image
import markdown
from ..config import settings
import functools
import shutil

def openfile(filename):
    filepath = os.path.join("app/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown.markdown(text)
    data = {
        "text": html
    }
    return data


def create_workspace(filename):
    """
    Return workspace path
    """
    # base directory
    work_dir = Path(settings.work_dir)
    request_id = Path('.'.join(filename.split('.')))
    workspace = work_dir / request_id
    if not os.path.exists(workspace):
        os.makedirs(workspace)
    else:
        print('replace')
        shutil.rmtree(workspace)
        os.makedirs(workspace)
        print('replace finish')
    return workspace

