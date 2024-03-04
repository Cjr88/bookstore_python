
import pytest
import django

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

@pytest.fixture(scope='session')
def django_db_setup():
    django.setup()