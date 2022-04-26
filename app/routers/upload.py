from fastapi import Request, Form, APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ..library.helpers import *

router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/upload", response_class=HTMLResponse)
def get_upload(request: Request):
    return templates.TemplateResponse('upload.html', context={'request': request})


@router.post("/form1", response_class=HTMLResponse)
def form_post1(request: Request, string: str = Form(...)):
    yourstring = string
    return templates.TemplateResponse('upload.html', context={'request': request, 'yourstring': yourstring})


@router.post("/upload/new/")
async def post_upload(rename:tuple, file: UploadFile = File(...)):
    print(rename)

    data_dict = eval(rename[0])
    new_name = data_dict['rename']

    print(data_dict['rename'])
    # filename
    original_file_name = Path( ''.join(str(file.filename).split('.')[:-1]))
    if new_name:
        new_file_name = Path(new_name+'.'+str(file.filename).split('.')[-1])
    else:
        new_file_name = Path(str(file.filename))
    print(file.filename)
    print(type(file.filename))

    # create the directory path using new file name
    workspace = create_workspace(file.filename)
    # image full path
    original_path = str(workspace / original_file_name)+'.txt'
    new_path = workspace / new_file_name

    with open(original_path, 'wb') as myfile:
        contents = await file.read()
        myfile.write(contents)
    print(new_path)
    with open(str(new_path), 'wb') as myfile:
        contents = await file.read()
        myfile.write(contents)

    if new_name:
        new_name = new_name+'.'+str(file.filename).split('.')[-1]
    else:
        new_name = file.filename
    print(new_name)
    data = {
        "original_name": file.filename,
        "new_name": new_name
    }
    return data
