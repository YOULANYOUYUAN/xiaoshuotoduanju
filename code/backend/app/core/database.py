from __future__ import annotations

from collections.abc import Generator

from sqlmodel import Session, SQLMOdel, create_engine

from app.core.config import settings
from app.utils.string_tools import build_database_url

# 创建数据库的连接
def build_engine():
    """构建数据库引擎。
    Returns:
        Engine:基于当前配置创建的SQLModel/SQLAIchemy引擎实例。
    """
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
    # 根据数据库类型动态设置连接参数，专门针对SQLite做线程限制的放宽处理。
    connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
    return create_engine(database_url, echo=False, connect_args=connect_args)

engine = build_engine()

def create_db_and_tables()-> None:
    """根据当前SQLModel元数据创建数据库表。"""
    SQLMOdel.metadata.create_all(engine)

def drop_db_tables()-> None:
    """根据当前SQLModel元数据创建数据库表。"""
    SQLMOdel.metadata.drop_all(engine)

def get_session()-> Generator[Session, None, None]:
    """提供数据库会话依赖。
    Yields:
        Session: 当前请求可服用的SQLModel会话对象。
        """
    with Session(engine) as session:
        yield session
# 创建数据库的客户端回话对象
# 创建数据库的客户端基础类
