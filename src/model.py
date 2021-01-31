from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from config import db
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()
metadata = Base.metadata


class Songs(db.Model):
    __tablename__ = 'Songs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __init__(self, data):
        self.name = data.get('name')
        self.duration = data.get('duration')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.updated_at = func.now()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Songs.query.all()

    @staticmethod
    def get_one(song_id):
        return Songs.query.get(song_id)


class Podcasts(db.Model):
    __tablename__ = 'Podcasts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime(timezone=True), server_default=func.now())
    host = db.Column(db.String(100), nullable=False)
    _participants = db.Column('participants', db.Text, nullable=True, )
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)

    @hybrid_property
    def participants(self):
        if self._participants:
            return self._participants.split(',')

    @participants.setter
    def participants(self, participants):
        if participants:
            self._participants = ",".join(participants)
        else:
            self._participants = None

    def __init__(self, data):
        self.name = data.get('name')
        self.duration = data.get('duration')
        self.host = data.get('host')
        self.participants = data.get('participants')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.updated_at = func.now()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Podcasts.query.all()

    @staticmethod
    def get_one(podcast_id):
        return Podcasts.query.get(podcast_id)


class Audiobooks(db.Model):
    __tablename__ = 'Audiobooks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __init__(self, data):
        self.title = data.get('title')
        self.author = data.get('author')
        self.narrator = data.get('narrator')
        self.duration = data.get('duration')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.updated_at = func.now()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Audiobooks.query.all()

    @staticmethod
    def get_one(audio_book_id):
        return Audiobooks.query.get(audio_book_id)
