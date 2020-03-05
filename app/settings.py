from sanic_envconfig import EnvConfig

class Settings(EnvConfig):
    DEBUG: bool = True
    DB_URL: str = ''