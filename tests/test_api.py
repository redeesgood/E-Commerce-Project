from faker import Faker
from api.api_client import APIClient

def test_create_user_api(api: APIClient):
    fake = Faker('ru_RU')
    
    random_name = fake.name()
    random_job = fake.job()
    
    response = api.create_user(random_name, random_job)
    data = response.json()
    
    assert response.status_code == 201, "Пользователь не создался"
    assert data["name"] == random_name, "Пользователя с таким именем не существует"
    assert data["job"] == random_job, "Пользователя с такой профессией не существует"