import fastapi

router = fastapi.APIRouter()


@router.get('/url')
def start_job():
    return {"Hello": "World"}


@router.get('/check_status')
def check_job_status():
    pass
