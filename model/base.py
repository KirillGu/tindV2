import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

#Кандидат
class Candidate(Base):
    __tablename__ = 'Candidate'

    id = sq.Column(sq.Integer, primary_key=True, unique=True)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)
    screen_name = sq.Column(sq.String)
    photos = relationship('Photo', backref='Candidate')
    users = relationship('User', secondary='user_to_candidate')

#Фото
class Photo(Base):
    __tablename__ = 'Photo'

    id = sq.Column(sq.String, primary_key=True, unique=True)
    photo_id = sq.Column(sq.Integer)
    candidate_id = sq.Column(sq.Integer, sq.ForeignKey('Candidate.id'))
    likes_count = sq.Column(sq.Integer)
    comments_count = sq.Column(sq.Integer)


class User(Base):
    __tablename__ = 'User'

    id = sq.Column(sq.Integer, primary_key=True, unique=True)
    token = sq.Column(sq.String)
    candidates = relationship('Candidate', secondary='user_to_candidate')


user_to_candidate = sq.Table(
    'user_to_candidate', Base.metadata,
    sq.Column('User_id', sq.Integer, sq.ForeignKey('User.id')),
    sq.Column('Candidate_id', sq.Integer, sq.ForeignKey('Candidate.id')),
)
