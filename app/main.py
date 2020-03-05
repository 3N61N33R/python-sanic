"""application entry point"""

from databases import Database
from environs import Env
from sanic import Sanic

from app.settings import Settings

app=Sanic(__name__)

def setup_database():
    app.db = Database(app.config.DB_URL)  

    #sanic listener to specify database connect operation
    @app.listener('after_server_start')    
    async def connect_to_db(*args, **kwargs):        
        await app.db.connect()

    #sanic listener to specify database dicconnect operation
    @app.listener('after_server_stop')    
    async def disconnect_from_db(*args, **kwargs):        
        await app.db.disconnect()

def init():
    env = Env()
    env.read_env()
    app.config.from_object(Settings)
    app.run(debug=app.config.DEBUG)
