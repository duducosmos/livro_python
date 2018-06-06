from  flask_login import UserMixin
from passlib.hash import sha256_crypt

from model import *

class User(UserMixin):

    def __init__(self, email, password):
        self.db = model()
        self.query = self.db(self.db.user.email == email)
        self.errorlogin = 0

        if self.query.isempty() is False:
            self.userid = self.query.select(self.db.user.id,
                                            self.db.user.password,
                                            self.db.user.name
                                            ).first()
            self.email = email
            self.name = self.userid.name
            self.password = password

    def get_id(self):
        if(self.query.isempty() is True):
            return None

        return self.email

    def is_active(self):
        return True

    def is_authenticated(self):
        if(self.query.isempty() is True):
            self.errorlogin = 1
            return False

        if sha256_crypt.verify(self.password, self.userid.password):
            return True

        self.errorlogin = 2
        return False

    def is_anonymous(self):
        return False

    @classmethod
    def get_user(cls, user_id):
        db = model()
        query = db(db.user.email == user_id)
        if query.isempty() is True:
            return None
        user = query.select(db.user.email, db.user.password).first()
        return cls(user.email, user.password)