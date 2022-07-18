import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):
    #prepare test
    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    #clean after test
    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", 123456)
        number = self.phonebook.lookup("Bob")
        self.assertEqual(123456, number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    
    def test_empty_ponebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob", "1234")
        self.phonebook.add("Anna", "01234")
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add("Bob", "1234")
        self.phonebook.add("Sue", "1234")
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob", "1234")
        self.phonebook.add("Sue", "123")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_adds_names_numbers(self):
        self.phonebook.add("Sue", "1222345")
        self.assertIn("1222345", self.phonebook.get_names())
        self.assertIn("Sue", self.phonebook.get_numbers())