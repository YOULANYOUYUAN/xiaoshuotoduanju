import sys
from pathlib import Path
from logging.config import fileConfig

# --- 🛠️ 核心修复：必须在导入 app 之前，把 backend 目录加入 sys.path ---
# 获取当前 env.py 所在的文件夹 (即 alembic 文件夹)
current_dir = Path(__file__).resolve().parent
# 获取 backend 目录 (即 alembic 的上一级目录)
backend_dir = current_dir.parent

if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))
# ---------------------------------------------------------

from sqlalchemy import create_engine, pool
from sqlmodel import SQLModel
from alembic import context

# 现在的路径已经包含 backend 了，可以安全导入
from app.core.config import settings
from app.utils.string_tools import build_database_url
from app.models import *  # 导入所有模型，确保 Alembic 能扫描到表结构<websource>source_group_web_1</websource>

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

database_url = build_database_url(
    db_engine=settings.db_engine,
    db_driver=settings.db_driver,
    db_host=settings.db_host,
    db_port=settings.db_port,
    db_name=settings.db_name,
    db_user=settings.db_user,
    db_password=settings.db_password,
    db_sqlite_path=settings.db_sqlite_path,
)
config.set_main_option("sqlalchemy.url", database_url)


# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = SQLModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(
        database_url,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()