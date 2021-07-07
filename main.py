import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy import func

from function import random_type, mac_generator, sorting
from sqlalchemy.orm import Session
from database import get_db
from models import Anagram, Devices, Endpoints

app = FastAPI()


@app.get('/anagram')
def get_word(word1: str, word2: str, db: Session = Depends(get_db)):
    """ Функция, которая проверяет являются ли слова анаграммами. Задание №1"""
    word1_list = sorting(word1)
    word2_list = sorting(word2)
    change_count = db.query(Anagram).filter(Anagram.id == 1).first()
    if word1_list == word2_list:
        change_count.count = change_count.count + 1

        db.commit()
        return {"anagram": True, "count": change_count.count}
    return {"anagram": False, "count": change_count.count}


@app.post("/create device", status_code=201)
def create_device(db: Session = Depends(get_db)):
    """Запрос для создания объекта в таблице devices. Задание №2"""
    to_create = Devices(
        dev_id=mac_generator(),
        dev_type=random_type(),
    )

    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": to_create.id
    }


@app.post("/group devices")
def group_devices(db: Session = Depends(get_db)):
    """Получаем список всех устройств, которые не привязаны к таблице endpoints и группируем их по типу устройств."""
    endpoints = db.query(Endpoints.device_id)
    group_tables = db.query(func.count(Devices.dev_type), Devices.dev_type).filter(~Devices.id.in_(endpoints)) \
        .group_by(Devices.dev_type).all()
    a = group_tables[0][0]
    return a


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
