from fastapi import APIRouter

router = APIRouter(
    prefix="/tech"
)


@router.get(
    path="/ready"
)
def ready():
    return


@router.get(
    path="/health"
)
def health():
    return
