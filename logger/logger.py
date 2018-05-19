import logging
from typing import Callable, Any, Tuple, Dict


def logger() -> logging.Logger:
    """Represent logger for console."""

    log = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    return log


def obj_log(log: logging.Logger) -> Callable[..., Any]:
    """Represent logger for a given object."""

    def decorator(original: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Tuple[Any, Any], **kwargs: Dict[Any, Any]) -> Callable[..., Any]:
            log.info('Performing %s operation', original.__name__)
            result = original(*args, **kwargs)
            log.info('Result equals to %s', result)
            return result
        return wrapper
    return decorator
