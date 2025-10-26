# main.py - ОБНОВЛЕННАЯ ВЕРСИЯ
from app.server import create_app
import logging
import os
from aiohttp import web

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def handle_index(request):
    return web.FileResponse('./static/index.html')

async def handle_history(request):
    return web.FileResponse('./static/history.html')

async def handle_agents(request):
    return web.FileResponse('./static/agents.html')

def create_app_with_static():
    app = create_app()
    
    # Добавляем статические маршруты
    app.router.add_get('/', handle_index)
    app.router.add_get('/index.html', handle_index)
    app.router.add_get('/history.html', handle_history)
    app.router.add_get('/agents.html', handle_agents)
    
    # Обслуживаем статические файлы
    app.router.add_static('/js/', path='./static/js/', show_index=True)
    
    return app

if __name__ == '__main__':
    app = create_app_with_static()
    
    logger.info("Запуск REST API сервера...")
    logger.info("Сервер будет доступен на http://localhost:8000")
    logger.info("Фронтенд доступен по:")
    logger.info("  http://localhost:8000/ - главная страница")
    logger.info("  http://localhost:8000/history.html - история")
    logger.info("  http://localhost:8000/agents.html - агенты")
    
    import aiohttp.web
    port = int(os.environ.get('PORT', '8000'))
    aiohttp.web.run_app(
        app,
        host='0.0.0.0',
        port=port
    )