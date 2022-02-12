from app import app_runner
from app.config.common import config

if __name__ == "__main__":
    flask_app = app_runner.create_app()
    flask_app.run(
        config.get("APP_HOST"),
        config.get("APP_PORT"),
        debug=config.get("APP_DEBUG"),
        threaded=True,
    )
