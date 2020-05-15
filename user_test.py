import unittest # Importing the unittest module
from user import User,Credential # Importing the User class and Credential class
import pyperclip

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

        self.assertEqual(self.new_user.first_name,"Samuel")
        self.assertEqual(self.new_user.last_name,"Kariuki")
        self.assertEqual(self.new_user.user_name,"mtoto")
        self.assertEqual(self.new_user.password,"456yWj.")

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

def test_display_account(self):
        """
        method that return a list of acounts
        """
        self.assertEqual(User.display_account(),User.user_list)
# other test cases here
def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple users
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","mtoto","785uemd,") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

# def test_delete_user(self):
#             '''
#             test_delete_user to test if we can remove a user from our user list
#             '''
#             self.new_user.save_user()
#             test_user = User("Test","user","mtoto","785uemd,") # new user
#             test_user.save_user()

#             self.new_user.delete_user()# Deleting a user object
#             self.assertEqual(len(User.user_list),1)

def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)


class TestCredential(unittest.TestCase): 
    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_credential=Credential('Twitter',"mtotowanursary","99278043")   
    def test_account_exist(self):
        """
        account_exist checks if account new_credintial exist
        """
        self.assertEqual(self.new_credential.user_name,"mtotowanursary")
       
    def test_save_credential(self):
        """
        To save new_credential_accont in the credential list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1) 
    def test_save_multiple_credential(self):
        """
        To test how to save multiple
        """
        self.new_credential.save_credential()
        test_credential=Credential('whatsapp',"mtotowanursary",'99278043')
        test_credential.save_credential()  

        self.assertEqual(len(Credential.credential_list),2)
    
    def test_delete_credential(self):
        """
        To test if credentail can be deleted
        """
        self.new_credential.save_credential()
        test_credential=Credential('twitter',"mtotowa",'99278043')
        test_credential.save_credential()  

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []
    def display_credential(self):
        """
        to test if credentials can be displayed using method
        """
        self.assertEqual(Credential.display_credentials(),Credential.credential_list)     


if __name__ ==  '__main__':
    unittest.main()