import requests
from fastapi import APIRouter

routers = []

coctail_router = APIRouter(prefix="/coctail")


@coctail_router.get("/search/{name}")
async def get_coctail(name: str):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}"
    response = requests.get(url)
    return response.json()


@coctail_router.get("/random")
async def get_random():
    url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    return response.json()


gender_router = APIRouter(prefix="/gender")


@gender_router.get("/{name}")
async def guess(name: str):
    url = f"https://api.genderize.io/?name={name}"
    res = requests.get(url)
    return res.json()


routers.append(coctail_router)
routers.append(gender_router)
