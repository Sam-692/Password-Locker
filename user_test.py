import unittest # Importing the unittest module
from user import User # Importing the contact class

class Testuser(unittest.TestCase):
        '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Samuel","kariuki","mtoto","456yWj.") # create user object


def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"Samuel")
        self.assertEqual(self.new_contact.last_name,"Kariuki")
        self.assertEqual(self.new_contact.user_name,"mtoto")
        self.assertEqual(self.new_contact.password,"456yWj.")


if __name__ == '__main__':
    unittest.main()