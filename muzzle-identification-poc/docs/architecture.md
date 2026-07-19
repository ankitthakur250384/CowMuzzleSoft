High level architecture follows recommended layered architecture: Presentation -> API Gateway -> Business -> Application -> Domain -> Infrastructure -> Data.

Components:
- Mobile Flutter app for image upload and viewing results
- FastAPI backend exposing /api/identify that runs AI pipeline
- Models: YOLO for muzzle detection, ResNet50 for embeddings, FAISS for nearest neighbor matching
- Postgres for metadata and Redis for cache
