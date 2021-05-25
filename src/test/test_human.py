import unittest

from humans.human import Human, Sex


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_valid_human(self):
        horst = Human(48, Sex.MALE, "Horsti")
        self.assertEqual(horst.age, 48)
        self.assertEqual(horst.sex, Sex.MALE)
        self.assertEqual(horst.name, "Horsti")

    def test_invalid_age_human(self):
        with self.assertRaises(ValueError):
            horst = Human(-48, Sex.MALE, "Horsti")

    def test_invalid_name_human(self):
        with self.assertRaises(ValueError):
            horst = Human(12, Sex.MALE, None)
        with self.assertRaises(ValueError):
            bernd = Human(12, Sex.FEMALE, "")


if __name__ == '__main__':
    unittest.main()
