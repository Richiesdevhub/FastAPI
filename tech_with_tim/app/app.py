from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts={1:{"title":"First Post", "content":"This is the first post"}, 
            2:{"title":"Second Post", "content":"This is the second post"},
            3: { "title": "Inflexión", "content": "La única constante en la vida es el cambio." },
            4: { "title": "Perspectiva", "content": "El paisaje cambia según el caminante." },
            5: { "title": "Reflexión", "content": "La lógica te llevará de la A a la Z, la imaginación te llevará a cualquier lugar." },
            6: { "title": "Sabiduría", "content": "No hay que apagar la luz del otro para que brille la nuestra." },
            7: { "title": "Esencia", "content": "La verdadera medida de un hombre no se ve en sus momentos de confort, sino en sus momentos de conflicto." },
            8: { "title": "Aventura", "content": "El mayor riesgo es no correr ningún riesgo." },
            9: { "title": "Trascendencia", "content": "El éxito no es el final, el fracaso no es la fatalidad: es el coraje lo que cuenta." },
            10: { "title": "Inspiración", "content": "El mejor momento para plantar un árbol fue hace 20 años. El segundo mejor momento es ahora." }
            }

@app.get("/posts")
def get_all_posts(limit:int=None):
    if limit:
        return {p: text_posts[p] for p in list(text_posts)[:limit]}
    return text_posts

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id, "Post not found")

@app.post("/posts")
def create_post(post: PostCreate)-> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post