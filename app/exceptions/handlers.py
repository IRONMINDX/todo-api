from fastapi import Request, Response
from fastapi.responses import JSONResponse

async def value_error_handler(request:Request,exc:ValueError):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": str(exc),
            "errors":[]
        })

async def global_exception_handler(request:Request,exc:Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error",
            "errors":[]
        })
