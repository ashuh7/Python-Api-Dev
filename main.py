from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel # for schema defination we use pydantic using fastapi 
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title:str   
    content:str
    published: bool = True
    rating: Optional[int] = None



@app.get("/")
async def root():
    return {"message": "Wooo Ye le laude...."}

# New path operation : Retrieving the bunch of social media posts from our application
@app.get("/posts")
def get_posts():
    return {"Data": "THis is your posts"}

# New path operation : Post the bunch of social media posts to our application
@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.rating)
    print(new_post.model_dump()) #converting pydantic model to dictionary can use .dict() too
    return {"data": new_post}
# title str, content str, category str, published bool