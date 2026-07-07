import logging
import time
from urllib import request
from fastapi import Request, responses

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)
async def log_middleware(request: Request, call_next):
    start_time = time.time()
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    execution_time = time.time() - start_time
    logger.info(f"{request.method} {request.url.path} {response.status_code} {execution_time:.4f}s")
    return response