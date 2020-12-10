from santa.db import db
from santa.base.models import Member


def insert_member_to_db(member_dict):
    try:
        db.session.add(Member(name=member_dict['name'], interest=member_dict['interest'], email=member_dict['email']))
        db.session.commit()
        return 1
    except KeyError:
        return 0
    except Exception as  err:
        print(err)
        return 0


def check_uniq_email(email):
    return Member.query.with_entities(Member.email).filter(Member.email == email).first()