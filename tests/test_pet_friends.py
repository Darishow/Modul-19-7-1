from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password)
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=' '):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert result


#10 тестов на методы, которых не было в примере: create_pet_simple и set_pet_photo
def test_create_pet_simple_with_valid_data():
    """Проверяем, что можно создать питомца с корректными данными"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, 'Барсик', 'Кот', 3)

    assert status == 200
    assert result['name'] == 'Барсик'
    assert result['animal_type'] == 'Кот'
    assert result['age'] == 3


def test_create_pet_simple_with_invalid_data():
    """Проверяем, что нельзя создать питомца с некорректными данными"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, '', 'Собака', -1)

    assert status == 400
    assert 'error' in result


def test_set_pet_photo_with_valid_data():
    """Проверяем, что можно установить фото питомца с корректными данными"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet = pf.get_list_of_pets(auth_key)
    pet_id = pet['pets'][0]['id']
    status, result = pf.set_pet_photo(auth_key, pet_id, 'path/to/photo.jpg')

    assert status == 200
    assert 'photo' in result


def test_set_pet_photo_with_invalid_data():
    """Проверяем, что нельзя установить фото питомца с некорректными данными"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet = pf.get_list_of_pets(auth_key)
    pet_id = pet['pets'][0]['id']
    status, result = pf.set_pet_photo(auth_key, pet_id, 'invalid/photo.jpg')

    assert status == 400
    assert 'error' in result


def test_create_pet_simple_without_auth_key():
    """Проверяем, что нельзя создать питомца без авторизационного ключа"""
    status, result = pf.create_pet_simple('', 'Барсик', 'Кот', 3)

    assert status == 401
    assert 'error' in result


def test_set_pet_photo_without_auth_key():
    """Проверяем, что нельзя установить фото питомца без авторизационного ключа"""
    _, pet = pf.get_list_of_pets(valid_auth_key)
    pet_id = pet['pets'][0]['id']
    status, result = pf.set_pet_photo('', pet_id, 'path/to/photo.jpg')

    assert status == 401
    assert 'error' in result


def test_create_pet_simple_with_empty_data():
    """Проверяем, что нельзя создать питомца с пустыми данными"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, '', '', '')

    assert status == 400
    assert 'error' in result


def test_set_pet_photo_with_nonexistent_pet():
    """Проверяем, что нельзя установить фото несуществующего питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf
    assert status == 404
    assert 'error' in result


def test_create_pet_simple_with_missing_parameters():
    """Проверяем, что нельзя создать питомца с недостающими параметрами"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name='Барсик')

    assert status == 400
    assert 'error' in result


def test_set_pet_photo_with_missing_parameters():
    """Проверяем, что нельзя установить фото питомца с недостающими параметрами"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet = pf.get_list_of_pets(auth_key)
    pet_id = pet['pets'][0]['id']
    status, result = pf.set_pet_photo(auth_key, pet_id)

    assert status == 400
    assert 'error' in result