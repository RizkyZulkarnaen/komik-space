from fastapi import APIRouter, Response
from datetime import date
import json

router = APIRouter(prefix='/manga')

d = [
    {"User": "Rizki", "date": date.today(), "count": 1},
    {"User": "zulkarnaen", "date": date.today(), "count": 2},
]

@router.get('/category')
async def category():
    json_str = json.dumps(d, indent=4, default=str)
    return Response(content=json_str, media_type='application/json')