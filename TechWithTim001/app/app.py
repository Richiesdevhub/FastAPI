from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy.future import select

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption:str=Form(""),
    session:AsyncSession=Depends(get_async_session),  
):
    post=Post(
        caption=caption,
        url="dummy url",
        file_type="photo",
        file_name="dummy name",
    )
    session.add(post)
    await session.commit() #habla a la db para guardar los datos de post
    await session.refresh(post) #Se refresta el post incluyendo el id y created_at generado por la db
    return post

@app.get("/feed")
async def get_feed(
    session:AsyncSession=Depends(get_async_session)
):
    result= await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts=[row[0] for row in result.all()]

    post_data=[]
    for post in posts:
        post_data.append(
            {
                "id":str(post.id),
                "caption":post.caption,
                "url":post.url,
                "file_type":post.file_type,
                "file_name":post.file_name,
                "created_at":post.created_at.isoformat()
            }
        )
    return {"post":post_data}