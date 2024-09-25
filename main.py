from fastapi import FastAPI
from pydantic import BaseModel
from controllers.AlternativeNewsArtcles import AlternativeNewsArticles
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,  # Allow credentials like cookies, authorization headers, etc.
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

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
    # print("Article is", article)  
    result = alternative_news.get_alternative_news_articles(article)
    # print("Result is", result)  
    return {"result": result}

@app.post("/news/url/")
def read_item(request_body: RequestBody):
    # print(request_body)
    article = request_body.url
    # print("Article is", article)  
    result = alternative_news.get_alternative_news_articles_by_url(article)
    # print("Result is", result)  
    return {"result": result}