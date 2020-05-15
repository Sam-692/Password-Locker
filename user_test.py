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

def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

# setup and class creation up here
def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

# other test cases here
def test_save_multiple_user(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","mtoto","785uemd,") # new contact
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

if __name__ == '__main__':
    unittest.main()