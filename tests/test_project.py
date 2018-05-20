import unittest

class TestProject(unittest.TestCase):

    def setUp(self):
        self.message = "hello"

    def testMessage(self):
        self.assertEqual(self.message, 'hello')
