import logging
import configparser
from pathlib import Path
import functools

from helpers.files_helper import find_project_root, get_log_dir_path


class Logger:
    """
    A class for setting up and using a logger.

    Methods:
        setup_logger(name) -> logging.Logger:
            A static method for setting up a logger with the specified name.
    """

    @staticmethod
    def setup_logger(name: str) -> logging.Logger:
        config_path = find_project_root(Path(__file__)) / 'config.ini'

        config = configparser.ConfigParser()
        config.read(config_path)

        level = config.get('logging', 'level', fallback='INFO')
        log_file_path = get_log_dir_path() / config.get('logging', 'log_file', fallback='app.log')

        numeric_level = getattr(logging, level.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError(f'Invalid log level: {level}')

        logger = logging.getLogger(name)
        logger.setLevel(numeric_level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        fh = logging.FileHandler(log_file_path)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        return logger


def log_method_call(logger):
    """
    A decorator that logs the entry and exit of a method.

    Args:
        logger (logging.Logger): The logger to use for logging messages.

    Returns:
        function: The decorator that can be used to decorate a method.
    """

    def method_decorator(func):
        """
        A decorator that wraps a method and logs the entry and exit of the method.

        Args:
            func (function): The method to wrap.

        Returns:
            function: The wrapped method.
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> object:
            """
            The wrapped method that logs the entry and exit of the method.

            Args:
                *args: The arguments to pass to the method.
                **kwargs: The keyword arguments to pass to the method.

            Returns:
                object: The result of calling the method.
            """
            class_name = args[0].__class__.__name__
            method_name = func.__name__
            args_str = ', '.join(repr(arg) for arg in args[1:])
            kwargs_str = ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
            all_args_str = ", ".join(filter(None, [args_str, kwargs_str]))
            logger.info(f"Calling method: {class_name}.{method_name} with args: ({all_args_str})")
            try:
                result = func(*args, **kwargs)
                # logger.info(f"Method {class_name}.{method_name} successful")
                return result
            except Exception as e:
                logger.exception(f"Error in method {class_name}.{method_name}: {e}")
                raise

        return wrapper

    return method_decorator


def log_all_methods(logger: logging.Logger):
    """
    A decorator that logs the entry and exit of all methods of a class.

    Args:
        logger (logging.Logger): The logger to use for logging messages.

    Returns:
        Callable: A decorator that can be used to decorate a class.
    """

    def class_decorator(cls) -> object:
        """
        A decorator that wraps a class and logs the entry and exit of all methods of the class.

        Args:
            cls (type): The class to wrap.

        Returns:
            type: The wrapped class.
        """
        for name, method in cls.__dict__.items():
            if callable(method):
                setattr(cls, name, log_method_call(logger)(method))
        return cls

    return class_decorator
