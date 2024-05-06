from fastapi import APIRouter, Depends, HTTPException, status
from services.metric import MetricService
from models.metric import MetricResponseModel
from util.response import APIResponse

router = APIRouter()


@router.get("/", response_model=MetricResponseModel)
async def fetch_system_metrics(
    service: MetricService = Depends(MetricService),
):
    try:
        metrics = await service.fetch_general()
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code,
            message=e.detail
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK,
        message="Fetch system metrics successfully.",
        data=metrics.model_dump()
    )
