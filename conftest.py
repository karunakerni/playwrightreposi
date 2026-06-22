import pytest


@pytest.fixture(scope="session")
def credentials_list(request):
    return request.param


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "base_url": "https://api.eventhub.rahulshettyacademy.com"}
