#levantar el servidor 
#uvicorn main:app --reload

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from api.home import router as home_router 

app = FastAPI()

#configuro directorio de archivos estaticos 
app.mount("/static", StaticFiles(directory="static"), name="static")

#configuro directorio de paginas dinamicas
templates = Jinja2Templates(directory="/templates")

# Agregar el router de usuarios a la aplicación
app.include_router(home_router, prefix="/api")

