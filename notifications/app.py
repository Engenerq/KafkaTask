from fastapi import FastAPI

from core.config import get_settings
from api.router import router as api_notifycatyons
from core.lifespan import lifespan


class Application:
    app: FastAPI

    def __init__(self):
        self._config = get_settings()
        self.create_app().include_router()

    def __call__(self, *args, **kwargs):
        return self.app

    def create_app(self):
        self.app = FastAPI(
            **self._config.fastapi_settings,
            lifespan=lifespan,
        )
        return self

    def include_router(self):
        self.app.include_router(api_notifycatyons)
        return self


app = Application()()
