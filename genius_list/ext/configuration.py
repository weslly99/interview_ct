from dynaconf import FlaskDynaconf


def init_app(app):
    """Configuration factory

    Args:
        app: instance of Flask
    """
    FlaskDynaconf(app)