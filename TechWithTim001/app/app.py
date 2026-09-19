from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts={1: {"title": "Post 1", "content": "Content of post 1"},
            2: {"title": "Post 2", "content": "Content of post 2"},
            3: {"title": "Post 3", "content": "Content of post 3"}
            }

@app.get("/hello_world")
def hello_world():
    return {"message": "Hello World"}

@app.get("/posts")
def get_all_posts(limit:int=None):
    if limit:
        return list(text_posts.values())[:limit]
    return list(text_posts.values())

@app.get("/posts/{id}")
def get_post(id:str)->list[PostResponse]:
    if id not in text_posts:
        return HTTPException(status_code=404, detail="Post not found")
       
    return text_posts.get(id)

@app.post("/posts")
def create_post(post:PostCreate)->PostResponse:
    new_post={"title":post.title, "content":post.content}
    text_posts[max(text_posts.keys())+1] = new_post
    return new_post