#multiple inheritance


class User(object):
    def __init__ (self, email):
        self.email = email
        
    def sign_in(self):
        print('logged in'