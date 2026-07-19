"""Download dataset from Kaggle kernel outputs for sashreekkumar/muzzle

This script will try to use the `kaggle` CLI if available. If not, it will try to use the
Python Kaggle API client (`kaggle` package). If neither is available, it prints
instructions for installing and configuring the Kaggle API credentials.

Requirements:
- Install CLI: `pip install kaggle` and ensure `kaggle` is on PATH, or
- Place your Kaggle API token at ~/.kaggle/kaggle.json, or set env vars KAGGLE_USERNAME and KAGGLE_KEY

Usage:
    python download_kaggle_dataset.py
"""
import os
import subprocess
import shutil
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2].parents[0] / 'storage' / 'dataset'
DATA_DIR.mkdir(parents=True, exist_ok=True)

KERNEL = 'sashreekkumar/muzzle'


def download_with_cli():
    cmd = [
        'kaggle', 'kernels', 'output', KERNEL,
        '-p', str(DATA_DIR),
        '--unzip'
    ]
    print('Running CLI command:', ' '.join(cmd))
    subprocess.check_call(cmd)


def download_with_api():
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except Exception as e:
        raise RuntimeError('kaggle Python package not available') from e

    api = KaggleApi()
    api.authenticate()
    print('Authenticated with Kaggle API, attempting to download kernel outputs...')
    # The KaggleApi exposes kernel output download functionality. We attempt to call it.
    try:
        api.kernels_output_download(KERNEL, path=str(DATA_DIR), unzip=True)
    except AttributeError:
        # Method name may differ across versions; raise informative error
        raise RuntimeError('Kaggle API client does not support kernel output download on this installation. Please install the kaggle CLI or update the package.')


def download():
    if shutil.which('kaggle'):
        try:
            download_with_cli()
            return
        except subprocess.CalledProcessError as e:
            print('kaggle CLI command failed:', e)

    # Try Python API
    try:
        download_with_api()
        return
    except Exception as e:
        print('Python Kaggle API download failed:', e)

    # Nothing worked
    msg = (
        '\nCould not find a working Kaggle downloader. Please install and configure the Kaggle API:\n'
        '1) Install: pip install kaggle\n'
        "2) Place your kaggle.json at ~/.kaggle/kaggle.json (create folder if needed) or set KAGGLE_USERNAME and KAGGLE_KEY env vars.\n"
        "3) Ensure the `kaggle` CLI is on your PATH, or the `kaggle` Python package is installed.\n"
        "Then re-run: python download_kaggle_dataset.py\n"
    )
    print(msg)


if __name__ == '__main__':
    download()
