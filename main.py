import uvicorn
from fastapi import FastAPI, Depends
from sqlmodel import Session, select, SQLModel
from db import get_session
from models.bands import Band
from models.sub_genres import Sub_Genre
from models.albums import Album
from models.members import Member

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Heavy F*cking Metal \m/"}


def create_generic(model):
    def create(item: model, session: Session = Depends(get_session)):
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    return create

def read_generic(model):
    def read(item_id: int, session: Session = Depends(get_session)):
        return session.get(model, item_id)
    return read

def update_generic(model):
    def update(item_id: int, item: model, session: Session = Depends(get_session)):
        db_item = session.get(model, item_id)
        if db_item:
            item_data = item.model_dump(exclude_unset=True)
            for key, value in item_data.items():
                setattr(db_item, key, value)
            session.add(db_item)
            session.commit()
            session.refresh(db_item)
            return db_item
        return {"error": f"{model.__name__} with id {item_id} not found"}
    return update

def delete_generic(model):
    def delete(item_id: int, session: Session = Depends(get_session)):
        item = session.get(model, item_id)
        if item:
            session.delete(item)
            session.commit()
        return {"ok": True}
    return delete

# Band CRUD
app.post("/bands/")(create_generic(Band))
app.get("/bands/{item_id}")(read_generic(Band))
app.put("/bands/{item_id}")(update_generic(Band))
app.delete("/bands/{item_id}")(delete_generic(Band))

# Sub_Genre CRUD
app.post("/sub_genres/")(create_generic(Sub_Genre))
app.get("/sub_genres/{item_id}")(read_generic(Sub_Genre))
app.put("/sub_genres/{item_id}")(update_generic(Sub_Genre))
app.delete("/sub_genres/{item_id}")(delete_generic(Sub_Genre))

# Album CRUD
app.post("/albums/")(create_generic(Album))
app.get("/albums/{item_id}")(read_generic(Album))
app.put("/albums/{item_id}")(update_generic(Album))
app.delete("/albums/{item_id}")(delete_generic(Album))

# Member CRUD
app.post("/members/")(create_generic(Member))
app.get("/members/{item_id}")(read_generic(Member))
app.put("/members/{item_id}")(update_generic(Member))
app.delete("/members/{item_id}")(delete_generic(Member))
