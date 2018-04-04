import logging
from typing import Callable, Any, Tuple, Dict


def logger() -> logging.Logger:
    """Represent logger for console."""

    log = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)
    return log


def obj_log(log: logging.Logger) -> Callable[..., Any]:
    """Represent logger for a given object."""

    def decorator(original: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Tuple[Any, Any], **kwargs: Dict[Any, Any]) -> Callable[..., Any]:
            cls_name = args[0].__class__.__name__
            log.info('Performing %s operation', cls_name)
            result = original(*args, **kwargs)
            return result
        return wrapper
    return decorator
