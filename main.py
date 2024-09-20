from fastapi import FastAPI
from pydantic import BaseModel
from controllers.AlternativeNewsArtcles import AlternativeNewsArticles

app = FastAPI()
alternative_news = AlternativeNewsArticles() 

class RequestBody(BaseModel):
    article: str

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