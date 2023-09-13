import requests
from api_secrets import API_KEY_ASSEMBLYAI
import sys

# upload file

upload_endp = "https://api.assemblyai.com/v2/upload"
endpoint = "https://api.assemblyai.com/v2/transcript"
filename = sys.argv[1]
headers = {'authorization': API_KEY_ASSEMBLYAI}


# filename = "/path/to/foo.wav"

def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    up_response = requests.post(upload_endp,
                                headers=headers,
                                data=read_file(filename))

    audio_url = up_response.json()['upload_url']
    return audio_url


# start transcribing
    # audio_url = response.json()['upload_url']

def transcribe(audio_url):
    transcript_request = {"audio_url": audio_url}
    transcript_response = requests.post(
        endpoint, json=transcript_request, headers=headers)
    job_id = transcript_response.json()['id']
    return job_id


audio_url = upload(filename)
transc_id = transcribe(audio_url)

print(transc_id)

# Set the headers for the request, including the API token and content type


# poll
def poll(transc_id):
	polling_endpoint = endpoint + '/' + transc_id
	polling_response = requests.get(polling_endpoint, headers=headers)
	return polling_response.json()


def get_transcription_url():
    transcript_id = transcribe()
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
         return data, None
        elif data['status'] == 'error':
         return data, "error"





# save
