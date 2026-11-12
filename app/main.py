from fastapi import FastAPI, HTTPException,Response, Request, status


app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
   return {
       "message": "Hello World"
   }


@app.get("/headers")
def headers_endpoint(request: Request, response: Response):
    user_agent = request.headers["user-agent"]
    accpet_language = request.headers["accept-language"]

    if not(user_agent and accpet_language):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Отсутвует верный заголовок"
        )

    return {
        "User-Agent": request.headers["user-agent"],
        "Accept-Language": request.headers["accept-language"]
    }
