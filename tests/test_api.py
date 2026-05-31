from faker import Faker
from api.api_client import APIClient


def test_create_user_api(api: APIClient):
    fake = Faker("ru_RU")

    random_name = fake.name()
    random_job = fake.job()

    response = api.create_user(random_name, random_job)
    data = response.json()

    assert response.status_code == 201, "Пользователь не создался"
    assert data["name"] == random_name, "Пользователя с таким именем не существует"
    assert data["job"] == random_job, "Пользователя с такой профессией не существует"


def test_get_user_api(api: APIClient):
    response = api.get_user(1)
    data = response.json()

    assert response.status_code == 200, "Пользователь не найден"
    assert data["data"]["id"] == 1, "Информации по пользователю не существует"


def test_delete_user_api(api: APIClient):
    response = api.delete_user(1)

    assert response.status_code == 204, "Пользователь не удалён"


def test_patch_user_api(api: APIClient):
    fake = Faker("ru_RU")

    random_name = fake.name()
    random_job = fake.job()

    response = api.patch_user(1, random_name, random_job)
    data = response.json()

    assert response.status_code == 200, "Ресурс не был обновлён"
    assert data["name"] == random_name, "Имя пользователя не соответствует ожидаемому"
    assert data["job"] == random_job, (
        "Профессия пользователя не соответствует ожидаемой"
    )
