import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from Chapter_1 import browsing

data = ["Ivan", "Petrov", "root@admin.ru"]

class TestRegistrationAbs(unittest.TestCase):
    def test_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browsing(link, data)

    def test_registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browsing(link, data)


if __name__ == "__main__":
    unittest.main()
