from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wooo Ye le laude...."}

# New path operation : Retrieving the bunch of social media posts from our application
@app.get("/posts")
def get_posts():
    return {"Data": "THis is your posts"}

# New path operation : Post the bunch of social media posts to our application
@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}