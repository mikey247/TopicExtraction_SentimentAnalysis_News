from fastapi import FastAPI
from pydantic import BaseModel
from controllers.AlternativeNewsArtcles import AlternativeNewsArticles
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

origins = [ "http://localhost:5173", "http://localhost:3000", "http://localhost:3000/", "http://localhost:5173/", "https://perspectify-rho.vercel.app", "http://perspectify-rho.vercel.app/", "https://perspectify-rho.vercel.app/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173/","https://perspectify-rho.vercel.app", "http://perspectify-rho.vercel.app/", "https://perspectify-rho.vercel.app/"],  # Allow all origins
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

alternative_news = AlternativeNewsArticles() 

class RequestBody(BaseModel):
    article: str
    source: str
    url: str

@app.get("/")
def read_root():
    return {"message": "Hi there!"}

@app.post("/news/")
def read_item(request_body: RequestBody):
    # print(request_body)
    article = request_body.article
    source = request_body.source
    # print("Article is", article)  
    result = alternative_news.get_alternative_news_articles(article, source)
    # print("Result is", result)  
    return {"result": result}

@app.post("/news/url/")
def read_item(request_body: RequestBody):
    # print(request_body)
    article = request_body.url
    source = request_body.source
    # print("Article is", article)  
    result = alternative_news.get_alternative_news_articles_by_url(article, source)
    # print(alternative_news.process_results(result))
    # print("Result is", result)  
    return {"result": result}