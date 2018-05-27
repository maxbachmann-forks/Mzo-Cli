import asyncio

from collections import Awaitable
from functools import wraps

import click


def async_command(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        if isinstance(result, Awaitable):
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(result)
        else:
            return result
    return wrapper


def command(name=None, cls=None, **attrs):
    def decorator(f):
        f = async_command(f)
        return click.command(name=name, cls=cls, **attrs)(f)
    return decorator


def group(name=None, **attrs):
    def decorator(f):
        f = async_command(f)
        return click.group(name=name, **attrs)(f)
    return decorator
