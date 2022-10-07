from typing import Optional, Union

from fastapi import APIRouter, status, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.responses import PlainTextResponse

from app.dto.pharse import Expression
from app.logic.parser import dijkstras_two_stack_algorithm

router = APIRouter()


@router.get("/")
async def index() -> str:
    return "Hello World"


@router.get("/eval", status_code=status.HTTP_200_OK)
async def eval_get_method(phrase: str) -> Union[PlainTextResponse, str]:
    """

    :param phrase: "(5 + (( 4 * 2 ) * ( 2 + 3 )))"
    :return: "(5 + (( 4 * 2 ) * ( 2 + 3 ))) = 45"
    """
    try:
        answer: int = dijkstras_two_stack_algorithm(phrase)
    except Exception as e:
        return PlainTextResponse(str(e), status_code=400)
    return ''.join([phrase, ' = ', str(answer)])


@router.post("/eval")
async def eval_post_method(phrase: Expression) -> JSONResponse:
    """
    :param phrase: "(5 + (( 4 * 2 ) * ( 2 + 3 )))"
    :return: {"phrase": "(5 + (( 4 * 2 ) * ( 2 + 3 )))", "answer": 45}
    """
    try:
        answer: int = dijkstras_two_stack_algorithm(phrase.phrase)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
    content: dict = jsonable_encoder({"phrase": phrase.phrase, "answer": answer})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=content)
