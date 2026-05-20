import pytest
from typing import Generator
from db.db_core import DBHelper
from api.api_client import APIClient

import os
from dotenv import load_dotenv
load_dotenv()

@pytest.fixture
def db() -> Generator[DBHelper, None, None]:
    db_helper = DBHelper(":memory:")
    db_helper.create_tables()
    
    yield db_helper
    
    db_helper.close()

@pytest.fixture
def api() -> Generator[APIClient, None, None]:
    api_key = os.getenv("REQRES_API_KEY")
    assert api_key is not None, "API ключ не найден!"
    
    api = APIClient(api_key)
    
    yield api