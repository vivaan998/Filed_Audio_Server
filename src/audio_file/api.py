from flask import Blueprint, make_response
from flask import request
from flask import jsonify
from src.audio_file.audio import AudiobooksAPI, SongsAPI, PodcastsAPI
from src.excecptions.app_exception import BadRequestException

bp_audio = Blueprint('audio_files', 'audio_files')


@bp_audio.route('/<audio_file_type>', methods=['GET'])
def get(audio_file_type):
    if audio_file_type == 'Songs':
        audio_files = SongsAPI.get_all_songs()

    elif audio_file_type == 'Podcasts':
        audio_files = PodcastsAPI.get_all_podcasts()

    elif audio_file_type == 'Audiobooks':
        audio_files = AudiobooksAPI.get_all_audio_books()

    else:
        raise BadRequestException({'error': 'Could not find the audio type, please check the url'})

    return make_response(jsonify(audio_files), 200)


@bp_audio.route('/<audio_file_type>/<audio_file_id>', methods=['GET'])
def get_audio_by_id(audio_file_type, audio_file_id):
    if audio_file_type == 'Songs':
        audio_file = SongsAPI.get_songs_by_id(audio_file_id)

    elif audio_file_type == 'Podcasts':
        audio_file = PodcastsAPI.get_podcast_by_id(audio_file_id)

    elif audio_file_type == 'Audiobooks':
        audio_file = AudiobooksAPI.get_audio_book_by_id(audio_file_id)

    else:
        raise BadRequestException({'error': 'Could not find the audio type, please check the url'})

    return make_response(jsonify(audio_file), 200)


@bp_audio.route('/', methods=['POST'])
def post():
    data = request.get_json()
    if data['audioFileType'] == 'Songs':
        audio = SongsAPI.create(data['audioFileMetadata'])

    elif data['audioFileType'] == 'Podcasts':
        audio = PodcastsAPI.create(data['audioFileMetadata'])

    elif data['audioFileType'] == 'Audiobooks':
        audio = AudiobooksAPI.create(data['audioFileMetadata'])

    else:
        raise BadRequestException({'error': 'No such audio type currently available.'})

    return make_response(jsonify(audio), 200)


@bp_audio.route('/<audio_file_type>/<audio_file_id>', methods=['PUT'])
def put(audio_file_type, audio_file_id):
    data = request.get_json()
    if audio_file_type == 'Songs':
        audio = SongsAPI.update(data['audioFileMetadata'], audio_file_id)

    elif audio_file_type == 'Podcasts':
        audio = PodcastsAPI.update(data['audioFileMetadata'], audio_file_id)

    elif audio_file_type == 'Audiobooks':
        audio = AudiobooksAPI.update(data['audioFileMetadata'], audio_file_id)

    else:
        raise BadRequestException({'error': 'Could not find the audio type, please check the url'})

    return make_response(jsonify(audio), 200)


@bp_audio.route('/<audio_file_type>/<audio_file_id>', methods=['DELETE'])
def delete(audio_file_type, audio_file_id):
    if audio_file_type == 'Songs':
        audio_file = SongsAPI.delete(audio_file_id)

    elif audio_file_type == 'Podcasts':
        audio_file = PodcastsAPI.delete(audio_file_id)

    elif audio_file_type == 'Audiobooks':
        audio_file = AudiobooksAPI.delete(audio_file_id)

    else:
        raise BadRequestException({'error': 'Could not find the audio type, please check the url'})

    return make_response(jsonify(audio_file), 200)
