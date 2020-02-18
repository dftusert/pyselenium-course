import unittest
from ch1_src_5_s11 import registration

class TestReg(unittest.TestCase):
    def test_rpage_first(self):
        self.assertEqual(registration("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!", "registration error at http://suninjuly.github.io/registration1.html")

    def test_rpage_second(self):
        self.assertEqual(registration("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!", "registration error at http://suninjuly.github.io/registration2.html")

if __name__ == "__main__":
    unittest.main()
