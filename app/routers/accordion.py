from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
import os
from os import listdir
from os.path import isfile, join
from datetime import date

router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/accordion", response_class=HTMLResponse)
def get_accordion(request: Request):
    upload_path = './static/upload'
    file_names = [f for f in listdir(upload_path)]
    #onlyfiles = [f for f in listdir(upload_path) if isfile(join(upload_path, f))]
    print(file_names)
    if  len(file_names) == 0:
        result = "Upload a file first to download"
        return templates.TemplateResponse('accordion.html', context={'request': request, 'result': result,
                                                                     'tag': 0})
    tag = file_names[0]
    result = "Select a file to download"
    return templates.TemplateResponse('accordion.html', context={'request': request, 'result': result,
                                                                 'tag': tag,'filenames' :file_names })


@router.post("/accordion", response_class=HTMLResponse)
def post_accordion(request: Request, tag: str = Form(...)):
    upload_path = './static/upload'
    filepath = upload_path+'/'+tag
    for f in listdir(filepath):
        if '.txt' in f:
            original_file_path = f
        else:
            new_file_path = f
    orginal_file_name = ''.join(original_file_path.split('.')[:-1])
    new_file_name = ''.join(new_file_path.split('.')[:-1])
    extension = new_file_path.split('.')[-1]
    date_str = date.today().strftime("%b-%d-%Y")
    download_file_name = orginal_file_name+'_'+new_file_name+'_'+date_str+'.'+extension
    newfile = [f for f in listdir(filepath) if '.txt' in f]
    print(newfile)
    return FileResponse(join(filepath,newfile[0]), media_type='application/octet-stream', filename=download_file_name)