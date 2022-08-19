import pytest


@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
        self.driver.get('https://vshkodin.com/')
        assert self.driver.title == "Vladimir Shkodin"
        