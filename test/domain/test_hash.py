import unittest

from src.domain.hash import Hash


class TestHash(unittest.TestCase):

    def test_should_return_key_mod(self):
        hash_object = Hash()
        self.assertEqual(hash_object.hash_function(3), 3, "Mod of key")
