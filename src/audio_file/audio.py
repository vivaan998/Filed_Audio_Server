import logging
from src.model import Audiobooks, Podcasts, Songs
from src.serializer import SongsSchema, PodcastsSchema, AudioBookSchema
from src.excecptions.app_exception import NotFoundException, ServerException, BadRequestException
from marshmallow import ValidationError

SONG_SCHEMA = SongsSchema()
PODCAST_SCHEMA = PodcastsSchema()
AUDIOBOOK_SCHEMA = AudioBookSchema()


class SongsAPI:

    @staticmethod
    def get_songs_by_id(song_id):
        song = Songs.get_one(song_id)
        if song:
            return SONG_SCHEMA.dump(song)
        else:
            raise NotFoundException({'error': 'Song with id ' + str(song_id) + ' not Found'})

    @staticmethod
    def get_all_songs():
        songs = Songs.get_all()
        if songs:
            return SONG_SCHEMA.dump(songs, many=True)
        else:
            return []

    @staticmethod
    def delete(song_id):
        try:
            song = Songs.get_one(song_id)
            if song:
                song.delete()
                return {'message': 'Deleted Successfully'}
            else:
                raise NotFoundException({'error': 'Song with id ' + str(song_id) + ' not Found'})

        except Exception as e:
            logging.error(e)
            raise ServerException({'error': 'Could not delete the file, please contact support'})

    @staticmethod
    def create(req_data):
        try:
            result = SONG_SCHEMA.load(req_data)
            song = Songs(result)
            song.save()
            return {'message': 'Saved Successfully'}

        except ValidationError as err:
            raise BadRequestException(err.messages)

    @staticmethod
    def update(req_data, song_id):
        try:
            result = SONG_SCHEMA.load(req_data)
            song = Songs.get_one(song_id)
            if song:
                song.update(result)
                return {'message': 'Updated Successfully'}
            else:
                raise NotFoundException({'error': 'Song with id ' + str(song_id) + ' not Found'})

        except ValidationError as err:
            raise BadRequestException(err.messages)


class AudiobooksAPI:

    @staticmethod
    def get_audio_book_by_id(audio_book_id):
        audio_book = Audiobooks.get_one(audio_book_id)
        if audio_book:
            return AUDIOBOOK_SCHEMA.dump(audio_book)
        else:
            raise NotFoundException({'error': 'Audiobook with id ' + str(audio_book_id) + ' not Found'})

    @staticmethod
    def get_all_audio_books():
        audio_books = Audiobooks.get_all()
        if audio_books:
            return AUDIOBOOK_SCHEMA.dump(audio_books, many=True)
        else:
            return []

    @staticmethod
    def delete(audio_book_id):
        try:
            audio_book = Audiobooks.get_one(audio_book_id)
            if audio_book:
                audio_book.delete()
                return {'message': 'Successfully Deleted'}
            else:
                raise NotFoundException({'error': 'Audiobook with id ' + str(audio_book_id) + ' not Found'})

        except Exception as e:
            logging.error(e)
            raise ServerException({'error': 'Could not delete the file, please contact support'})

    @staticmethod
    def create(req_data):
        try:
            result = AUDIOBOOK_SCHEMA.load(req_data)
            audio_book = Audiobooks(result)
            audio_book.save()
            return {'message': 'Saved Successfully'}

        except ValidationError as err:
            raise BadRequestException(err.messages)

    @staticmethod
    def update(req_data, audio_book_id):
        try:
            result = AUDIOBOOK_SCHEMA.load(req_data)
            audio_book = Audiobooks.get_one(audio_book_id)
            if audio_book:
                audio_book.update(result)
                return {'message': 'Updated Successfully'}
            else:
                raise NotFoundException({'error': 'Audiobook with id ' + str(audio_book_id) + ' not Found'})

        except ValidationError as err:
            raise BadRequestException(err.messages)


class PodcastsAPI:

    @staticmethod
    def get_podcast_by_id(podcast_id):
        podcast = Podcasts.get_one(podcast_id)
        if podcast:
            return PODCAST_SCHEMA.dump(podcast)
        else:
            raise NotFoundException({'error': 'Podcast with id ' + str(podcast_id) + ' not Found'})

    @staticmethod
    def get_all_podcasts():
        podcasts = Podcasts.get_all()
        if podcasts:
            return PODCAST_SCHEMA.dump(podcasts, many=True)
        else:
            return []

    @staticmethod
    def delete(podcast_id):
        try:
            podcast = Podcasts.get_one(podcast_id)
            if podcast:
                podcast.delete()
                return {'message': 'Successfully Deleted'}
            else:
                raise NotFoundException({'error': 'Podcast with id ' + str(podcast_id) + ' not Found'})

        except Exception as e:
            logging.error(e)
            raise ServerException({'error': 'Could not delete the file, please contact support'})

    @staticmethod
    def create(req_data):
        try:
            result = PODCAST_SCHEMA.load(req_data)
            podcast = Podcasts(result)
            podcast.save()
            return {'message': 'Saved Successfully'}

        except ValidationError as err:
            raise BadRequestException(err.messages)

    @staticmethod
    def update(req_data, podcast_id):
        try:
            result = PODCAST_SCHEMA.load(req_data)
            podcast = Podcasts.get_one(podcast_id)
            if podcast:
                podcast.update(result)
                return {'message': 'Updated Successfully'}
            else:
                raise NotFoundException({'error': 'Podcast with id ' + str(podcast_id) + ' not Found'})

        except ValidationError as err:
            raise BadRequestException(err.messages)
