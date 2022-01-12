import pytest


@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
        self.driver.get('https://www.delrayo.tech')
        assert self.driver.title == "DelRayo.tech - Delrayo Tech"
    
    def test_title_blog(self):
        self.driver.get('https://www.delrayo.tech/blog')
        print(self.driver.title)
        