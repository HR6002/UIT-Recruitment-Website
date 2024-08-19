from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.mount("/static", StaticFiles(directory="myenv/static"), name="static")

templates = Jinja2Templates(directory="myenv/templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about")
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/privacy")
async def read_privacy(request: Request):
    return templates.TemplateResponse("privacy.html", {"request": request})



@app.get("/contact")
async def read_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})



@app.get("/reviews")
async def read_contact(request: Request):
    return templates.TemplateResponse("reviews.html", {"request": request})


@app.get("/start")
async def read_contact(request: Request):
    return templates.TemplateResponse("start.html", {"request": request})


@app.get("/tc")
async def read_contact(request: Request):
    return templates.TemplateResponse("tc.html", {"request": request})






if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)