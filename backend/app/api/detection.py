from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from pathlib import Path
import uuid

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/detect")
async def detect_muzzle(file: UploadFile = File(...)):
    # Save uploaded file
    suffix = Path(file.filename).suffix or ".jpg"
    dest = UPLOAD_DIR / f"{uuid.uuid4().hex}{suffix}"
    contents = await file.read()
    dest.write_bytes(contents)

    # Placeholder: call detection model here and return bounding boxes
    # For now return a fake detection
    detection = {
        "file": str(dest),
        "detections": [
            {"label": "muzzle", "confidence": 0.98, "box": [50, 60, 200, 220]}
        ]
    }
    return JSONResponse(content=detection)
