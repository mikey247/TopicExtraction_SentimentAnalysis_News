from fastapi import FastAPI
from pydantic import BaseModel
from controllers.AlternativeNewsArtcles import AlternativeNewsArticles
from controllers.SentimentAnalysis import SentimentAnalysis
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

origins = [
    "http://topicextraction-sentimentanalysis-news.onrender.com/news/url",
    "https://topicextraction-sentimentanalysis-news.onrender.com/news/url",
    "http://localhost:5173", "http://localhost:3000", "http://localhost:3000/",
    "http://localhost:5173/", "https://perspectify-rho.vercel.app",
    "http://perspectify-rho.vercel.app/", "https://perspectify-rho.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["X-Requested-With", "Content-Type"],
)

alternative_news = AlternativeNewsArticles() 
sentiment_analysis = SentimentAnalysis()

class RequestBody(BaseModel):
    article: str
    source: str
    url: str

@app.get("/")
def read_root():
    return {"message": "Hi there!"}

@app.post("/news/")
def read_item(request_body: RequestBody):
    article = request_body.article
    source = request_body.source
    result = alternative_news.get_alternative_news_articles(article, source)
    alternative_news.process_results(result)
    return {"result": result, "source": source, "source_bias":sentiment_analysis.get_source_bias(source)}

@app.post("/news/url/")
def read_item(request_body: RequestBody):
    article = request_body.url
    source = request_body.source
    result = alternative_news.get_alternative_news_articles_by_url(article, source)
    alternative_news.process_results(result)
    return {"result": result, "source": source, "source_bias":sentiment_analysis.get_source_bias(source)}