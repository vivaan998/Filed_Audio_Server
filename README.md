# Audio File Server to save audio based on the type 
# FILED PROGRAMMING EXERCISE

## Requirements

This Project is developed using **Flask** and **SQLAlchemy**.

## How to run project locally

Clone repository and got to project's root directory afterwards follow steps:

1. Activate python virtual environment <br />
`source /path/to/local/env/activate`


2. Install requirements <br />
`pip install -r requirements.txt`
   

3. Create Database schema named `audio-file-server` <br />
   
   -    To use pre-populated data for testing, go to   
        Sql directory and use the dump to populate data.
        
   
4. Run app <br />
`python app.py`
   

## Structure

```

├── app.py                  # Application entry point
├── sql                     # SQL dump to init database and tables
├── config.py               # includes configurations for DB                                        
├── src
│    └──audio-file
│    │    └── api.py              # REST api definition
│    │    └── audio.py            # Core functions
│    │exceptions
│    │    └── app_exception.py    # Execptions are written over here
│    └──models.py                 # SQLAlchemy models
│    └──serializer.py             # Serializing the input and output data
├── test
     └── postman                 # Includes Postman tests
```
## GET ──>  /api/v1/audio-files/<audio_type>

Shows the list of all the audios in that audio_type from the local database.

## POST ──> /api/v1/audio-files/

Fetches the audio_type and audio_meta_data from request api and save it in the particular table of the local database.

## DELETE ──> /api/v1/audio-files/<audio_type>/<audio_file_id>

Deletes the record of the requested type and requested id from the respective table.  

## Update ──> /api/v1/audio-files/<audio_type>/<audio_file_id>

updates the record of the requested type and requested id from the respective table.

## GetByID ──> /api/v1/audio-files/<audio_type>/<audio_file_id>

Fetches the requested type and requested id data from the respective table.
