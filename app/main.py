from fastapi.openapi.models import Response
from starlette import status

from app.api.base import init_fast_api
from app.settings import settings
from app.api.epg.api import api_router
from app.dto.health_state import HealthState


async def health_check_handler(response: Response) -> HealthState:
    """
    :param response:
    :return:
    """
    response.status_code = status.HTTP_200_OK
    return HealthState(state="OK")


app = init_fast_api(settings, api_router, lambda: HealthState(state="OK"))

