from aiogram import Router

from . import event, menu, start


def setup_routers() -> Router:
    from . import about

    router = Router()
    router.include_router(start.router)
    router.include_router(menu.router)
    router.include_router(about.router)
    router.include_router(event.router)
    return router