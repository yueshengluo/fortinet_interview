### Task Description
Create a file upload / download web application with the requirements specified below.  

- The main purpose of this project is to allow users to upload multiple files. Make the UI look nice  and user friendly. You can use any framework, library, or write your own code.   Users can only upload CSS, JavaScript and HTML file. File size must be between 1 KB and 10MB,  it can be verified before or after uploading.
- Users can edit file names for each file before uploading. The physical name of the uploaded file  on the server should be the edited name.  
- The user must be able to see the original and edited file names after submitting. The user can  download these files. The downloaded file name should be original file name + underscore +  edited file name +underscore + downloaded date + extension. (You can use cookies, sessions,  files or variables for storing original file name)

### How to use
Go to the Upload and Download page on the top left of the navigation bar

### Template source
- [How to Build a Drag & Drop Form with FastAPI & JavaScript](https://towardsdatascience.com/how-to-build-a-drag-drop-form-with-python-javascript-f5e43433b005)

## Requirement

- Python 3.9.6
- See requirements.txt.

## Installation & Usage

Get your Unsplash API and put it in the `.env` file.

```bash
$ git clone git@github.com:yueshengluo/fortinet_interview.git
# change the directory
$ cd fortinet_interview
# install packages
$ pip install -r requirements.txt
# start the server
$ uvicorn app.main:app --reload --port 8000
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/).