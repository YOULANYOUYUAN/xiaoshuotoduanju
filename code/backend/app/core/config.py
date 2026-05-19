from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

# 提取项目根目录路径
BASE_DIR= Path(__file__).resolve().parents[3]
# 拼接.env的路径，斜杠有拼接作用
ENV_FILE = BASE_DIR/".env"
# 加载.env中的环境变量，override是环境有冲突是否要覆盖
load_dotenv(ENV_FILE, override=False)

# 冻结属性值，不允许配置类Settings实例化以后，被其他地方的程序修改
@dataclass(frozen=True)
class Settings(object):
    """项目运行时配置对象，一次加载，后续如果改.env，不会被加载"""
    app_name: str = field(default_factory=lambda: os.getenv("APP_NAME", "App"))
    app_description: str = field(default_factory=lambda: os.getenv("APP_DESCRIPTION", "App description"))
    app_env: str = field(default_factory=lambda: os.getenv("APP_ENV", "development"))
    host: str = field(default_factory=lambda: os.getenv("HOST", "0.0.0.0"))
    port: int = field(default_factory=lambda: int(os.getenv("PORT", "8000")))
    api_prefix: str = field(default_factory=lambda: os.getenv("API_PREFIX", "/api"))
    oss_root: str = field(default_factory=lambda: os.getenv("OSS_ROOT", "./data/oss"))
    db_engine: str = field(default_factory=lambda: os.getenv("DB_ENGINE", "postgres"))
    db_driver: str = field(default_factory=lambda: os.getenv("DB_DRIVER", "psycopg"))
    db_host: str = field(default_factory=lambda: os.getenv("DB_HOST", "127.0.0.1"))
    db_port: int = field(default_factory=lambda: int(os.getenv("DB_PORT", "5432")))
    db_name: str = field(default_factory=lambda: os.getenv("DB_NAME", "anonforge"))
    db_user: str = field(default_factory=lambda: os.getenv("DB_USER", "anonforge"))
    db_password: str = field(default_factory=lambda: os.getenv("DB_PASSWORD", "anonforge"))
    db_sqlite_path: str = field(default_factory=lambda: os.getenv("DB_SQLITE_PATH", "./data/app.db"))
    tz: str = field(default_factory=lambda: os.getenv("TZ", "Asia/Shanghai"))
    postgres_image: str = field(default_factory=lambda: os.getenv("POSTGRES_IMAGE", "postgres:18-alpine"))
    postgres_container_name: str = field(default_factory=lambda: os.getenv("POSTGRES_CONTAINER_NAME", "anonforge_dev_postgres"))
    postgres_host_port: int = field(default_factory=lambda: int(os.getenv("POSTGRES_HOST_PORT", "5432")))
    db_data_path: str = field(default_factory=lambda: os.getenv("DB_DATA_PATH", "./postgres/data"))
    db_healthcheck_interval: str = field(default_factory=lambda: os.getenv("DB_HEALTHCHECK_INTERVAL", "10s"))
    db_healthcheck_timeout: str = field(default_factory=lambda: os.getenv("DB_HEALTHCHECK_TIMEOUT", "5s"))
    db_healthcheck_retries: int = field(default_factory=lambda: int(os.getenv("DB_HEALTHCHECK_RETRIES", "5")))

settings = Settings()