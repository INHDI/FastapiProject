from typing import Union
import uvicorn
from fastapi import FastAPI
from logger.logger import logger_init
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

global user
user = "_"
app = FastAPI(title="api")

@app.get("/")
async def read_root():
    # get user from request
    logger_init.info(
        "Hello World", 
        extra={"user": user}
    )
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    config = uvicorn.Config("main:app", 
                            port=5000, 
                            log_level="info", 
                            reload=True)
    server = uvicorn.Server(config)
    # check startup server
    logger_init.info(
        "Server started ...", 
        extra={"user": user}
    )
    server.run()
    
