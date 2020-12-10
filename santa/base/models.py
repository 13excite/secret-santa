from santa.db import db


class Member(db.Model):
    __tablename__ = 'members'

    member_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    interest = db.Column(db.String(254))
    email = db.Column(db.String(150), unique=True)

    def __init__(self, name, interest, email):
        self.name = name
        #self.member_id = member_id
        self.interest = interest
        self.email = email

    def __repr__(self):
        return f'<Category {self.member_id}>'
