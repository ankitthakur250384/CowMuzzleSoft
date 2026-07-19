from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from ..services.identify_service import identify_muzzle

router = APIRouter(prefix="/api")

@router.post('/identify')
async def identify(file: UploadFile = File(...)):
    # save upload to storage/uploads
    content = await file.read()
    from pathlib import Path
    path = Path(__file__).resolve().parents[3] / 'storage' / 'uploads'
    path.mkdir(parents=True, exist_ok=True)
    file_path = path / file.filename
    with open(file_path, 'wb') as f:
        f.write(content)

    result = identify_muzzle(str(file_path))
    return JSONResponse(content=result)
