# app/routes/__init__.py
from .checks import checks_routes
from .agents import agent_routes

__all__ = ['checks_routes', 'agent_routes']