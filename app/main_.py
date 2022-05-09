from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from psycopg2.extras import RealDictCursor
import psycopg2
import time


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


while True:
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect(host="127.0.0.1", database='fastapi', user='postgres', password='postgres', cursor_factory=RealDictCursor)

        # Open a cursor to perform database operations
        cursor = conn.cursor()
        print('Database connection was successfull.')
        break
    except Exception as error:
        print("Connection to database failed.")
        print(error)
        time.sleep(5)


app = FastAPI()

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {'data': posts}

@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", [id])
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f'Post with id {id} not found!')
    return post

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts(title, content, published) VALUES(%s, %s, %s) RETURNING * """,
    (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {'message': 'successfully created posts', 'data': new_post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post = get_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f'Post with id {id} not found!')
    else:
        cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", [id])
        post = cursor.fetchone()
        conn.commit()
        print(post)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(post: Post, id: int):
    post_data = get_post(id)
    if not post_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f'Post with id {id} not found!')
    else:
        cursor.execute("""UPDATE posts SET title = %s, content = %s, published=%s WHERE id = %s RETURNING * """, [post.title, post.content, post.published, id])
        post = cursor.fetchone()
        conn.commit()
    return {"message": "update complete", "data": post}

