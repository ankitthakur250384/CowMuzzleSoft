"""
Recreate project directory structure for CowMuzzleSoft workspace.
This script creates directories and placeholder files if they don't already exist.
Run from repository root.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Directory list (relative to ROOT)
dirs = [
    "docs/images",
    "configs",
    "datasets/raw",
    "datasets/annotations",
    "datasets/processed",
    "datasets/train",
    "datasets/validation",
    "datasets/test",
    "datasets/sample",
    "models/detection",
    "models/recognition",
    "models/segmentation",
    "models/checkpoints",
    "models/pretrained",
    "ai/detection",
    "ai/preprocessing",
    "ai/recognition",
    "ai/search",
    "ai/evaluation",
    "ai/common",
    "backend/app/api",
    "backend/app/services",
    "backend/app/database/migrations",
    "backend/app/schemas",
    "backend/app/middleware",
    "backend/app/core",
    "backend/tests",
    "frontend/web/src",
    "frontend/web/public",
    "frontend/mobile/lib",
    "database/migrations",
    "scripts",
    "deployments/docker",
    "deployments/kubernetes",
    "deployments/nginx",
    "deployments/monitoring",
    "tests/unit",
    "tests/integration",
    "tests/performance",
    "examples",
]

# Files to create with minimal content (relative to ROOT)
files = {
    "docs/architecture.md": "# Architecture\n\nProject architecture overview.\n",
    "docs/api.md": "# API\n\nAPI documentation.\n",
    "docs/training.md": "# Training\n\nTraining instructions.\n",
    "docs/deployment.md": "# Deployment\n\nDeployment steps.\n",
    "docs/datasets.md": "# Datasets\n\nDataset layout.\n",
    "docs/benchmark.md": "# Benchmark\n\nBenchmark instructions.\n",
    "configs/development.yaml": "# development config\n",
    "configs/production.yaml": "# production config\n",
    "configs/detection.yaml": "# detection config\n",
    "configs/recognition.yaml": "# recognition config\n",
    "configs/database.yaml": "# database config\n",
    "ai/detection/train.py": "# train detector placeholder\n",
    "ai/detection/predict.py": "# detector predict placeholder\n",
    "ai/detection/export.py": "# export model placeholder\n",
    "ai/detection/dataset.py": "# dataset handling placeholder\n",
    "ai/detection/augmentations.py": "# augmentations placeholder\n",
    "ai/detection/utils.py": "# utils placeholder\n",
    "ai/preprocessing/crop.py": "# crop helper\n",
    "ai/preprocessing/enhance.py": "# enhance helper\n",
    "ai/preprocessing/normalize.py": "# normalize helper\n",
    "ai/preprocessing/quality.py": "# quality checks\n",
    "ai/preprocessing/alignment.py": "# alignment\n",
    "ai/recognition/train.py": "# recognition training\n",
    "ai/recognition/inference.py": "# recognition inference\n",
    "ai/recognition/embedding.py": "# embedding extractor\n",
    "ai/recognition/siamese.py": "# siamese network\n",
    "ai/recognition/arcface.py": "# arcface implementation\n",
    "ai/recognition/metrics.py": "# metrics\n",
    "ai/search/faiss_index.py": "# faiss index helper\n",
    "ai/search/search.py": "# search helper\n",
    "ai/search/update_index.py": "# update index\n",
    "ai/evaluation/detection_metrics.py": "# detection metrics\n",
    "ai/evaluation/recognition_metrics.py": "# recognition metrics\n",
    "ai/evaluation/benchmark.py": "# benchmark runner\n",
    "ai/common/logger.py": "# logger helper\n",
    "ai/common/config.py": "# config helper\n",
    "ai/common/visualization.py": "# visualization helpers\n",
    "ai/common/utils.py": "# common utilities\n",
    "backend/app/api/auth.py": "# auth api\n",
    "backend/app/api/cows.py": "# cows api\n",
    "backend/app/api/identification.py": "# identification api\n",
    "backend/app/api/registration.py": "# registration api\n",
    "backend/app/api/health.py": "# health check api\n",
    "backend/app/api/search.py": "# search api\n",
    "backend/app/services/detector.py": "# detector service\n",
    "backend/app/services/recognizer.py": "# recognizer service\n",
    "backend/app/services/embedding.py": "# embedding service\n",
    "backend/app/services/image_service.py": "# image service\n",
    "backend/app/services/faiss_service.py": "# faiss service\n",
    "backend/app/database/models.py": "# DB models\n",
    "backend/app/database/session.py": "# DB session helper\n",
    "backend/app/database/repository.py": "# repository\n",
    "backend/app/schemas/__init__.py": "# schemas package\n",
    "backend/app/core/__init__.py": "# core package\n",
    "backend/app/main.py": "# backend main entrypoint\n",
    "frontend/web/package.json": "{\n  \"name\": \"cowmuzzle-web\"\n}\n",
    "frontend/mobile/pubspec.yaml": "name: cowmuzzle_mobile\n",
    "database/schema.sql": "-- schema placeholder\n",
    "database/seed.sql": "-- seed placeholder\n",
    "scripts/prepare_dataset.py": "# prepare dataset script\n",
    "scripts/train_detector.py": "# train detector script\n",
    "scripts/train_recognizer.py": "# train recognizer script\n",
    "scripts/export_models.py": "# export models script\n",
    "scripts/build_faiss.py": "# build faiss index script\n",
    "scripts/evaluate.py": "# evaluate script\n",
    "examples/register_cow.py": "# example: register cow\n",
    "examples/identify_cow.py": "# example: identify cow\n",
    "examples/batch_identification.py": "# example: batch identification\n",
}


def create_structure():
    created_dirs = 0
    created_files = 0

    for d in dirs:
        p = ROOT / d
        if not p.exists():
            p.mkdir(parents=True, exist_ok=True)
            created_dirs += 1

    for rel_path, content in files.items():
        p = ROOT / rel_path
        p.parent.mkdir(parents=True, exist_ok=True)
        if not p.exists():
            p.write_text(content, encoding="utf-8")
            created_files += 1

    print(f"Created {created_dirs} directories and {created_files} files under {ROOT}")


if __name__ == "__main__":
    create_structure()