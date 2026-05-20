from faker import Faker
from api.api_client import APIClient

import os
from dotenv import load_dotenv
load_dotenv()

def test_create_user_api():
    api_key = os.getenv("REQRES_API_KEY")
    assert api_key is not None, "API ключ не найден!"
    
    api = APIClient(api_key)
    fake = Faker('ru_RU')
    
    random_name = fake.name()
    random_job = fake.job()
    
    response = api.create_user(random_name, random_job)
    data = response.json()
    
    assert response.status_code == 201, "Пользователь не создался"
    assert data["name"] == random_name, "Пользователя с таким именем не существует"
    assert data["job"] == random_job, "Пользователя с такой профессией не существует"