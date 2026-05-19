import pytest
from typing import Generator
from db.db_core import DBHelper

@pytest.fixture
def db() -> Generator[DBHelper, None, None]:
    db_helper = DBHelper(":memory:")
    db_helper.create_tables()
    
    yield db_helper
    
    db_helper.close()