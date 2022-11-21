import fastapi

router = fastapi.APIRouter()


@router.get("/sections/{id}")
async def read_section():
    return {'courses': []}


@router.get("/sections/{id}/content-block")
async def read_section_content_blocks():
    return {'course': []}


@router.get("/content-blocks/{id}")
async def read_content_block():
    return {"courses": []}
