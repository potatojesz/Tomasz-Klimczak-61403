import unittest
import encryption


class TestEncryption(unittest.TestCase):
    PLAIN_TEST_STRING = "to jest moj tekst"
    ENCRYPTED_PLAIN_TEST_STRING = "ta jist maj tikst"

    def testEncryption(self):
        assert encryption.encrypt(self.PLAIN_TEST_STRING) == self.ENCRYPTED_PLAIN_TEST_STRING, "Encrypt does not work!"

    def testDecryption(self):
        assert encryption.decrypt(self.ENCRYPTED_PLAIN_TEST_STRING) == self.PLAIN_TEST_STRING, "Decrypt does not work!"
