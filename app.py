from app import app_runner
from app.config.common import config

if __name__ == "__main__":
    flask_app = app_runner.create_app()
    flask_app.run("0.0.0.0", 12000, debug=config.get(
        "APP_DEBUG"), threaded=True)
