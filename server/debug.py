import ipdb
from app import app
from models import Game

if __name__ == "__main__":
    app_ctx = app.app_context()
    app_ctx.push()
    ipdb.set_trace()