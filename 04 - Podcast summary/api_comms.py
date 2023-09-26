
import requests
from api_secrets import API_KEY_ASSEMBLYAI
from api_secrets import API_KEY_LISTENNOTES
import json
import time
import pprint


headers = {'authorization': API_KEY_ASSEMBLYAI}
endpoint = "https://api.assemblyai.com/v2/transcript"

listennotes_episode_endpoint = "https://listen-api.listennotes.com/api/v2/episodes"
listennotes_headers = {'X-ListenAPI-Key': API_KEY_LISTENNOTES}


def get_episode_audio_url(episode_id):
    url = listennotes_episode_endpoint + '/' + episode_id
    response = requests.request('GET', url, headers=listennotes_headers)

    data = response.json()
    pprint.pprint(data)

    audio_url = data['audio']
    episode_thumbnail = data['thumbnail']
    podcast_title = data['podcast']['title']
    episode_title = data['title']

    return audio_url, episode_thumbnail, episode_title, podcast_title


# 96d84944f2744f96ac33357653e5f68e

# start transcribing
# audio_url = response.json()['upload_url']

def transcribe(audio_url, auto_chapters):
    transcript_request = {
        "audio_url": audio_url,
        "auto_chapters": auto_chapters
    }
    transcript_response = requests.post(
        endpoint, json=transcript_request, headers=headers)
    return transcript_response.json()['id']
    # return job_id


# audio_url = upload(filename)
# transc_id = transcribe(audio_url)

# print(transc_id)

# Set the headers for the request, including the API token and content type


# poll
def poll(transc_id):
    polling_endpoint = endpoint + '/' + transc_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()


def get_transcription_url(url, auto_chapters):
    transcript_id = transcribe(url, auto_chapters)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']

        print("Waiting 60 seconds")
        time.sleep(60)


def save_transcript(episode_id):
    audio_url, episode_thumbnail, episode_title, podcast_title = get_episode_audio_url(
        episode_id)
    data, error = get_transcription_url(audio_url, auto_chapters=True)

    pprint.pprint(data)

# 1:24:23 - This works so far

    if data:
        text_filename = episode_id + ".txt"
        with open(text_filename, "w") as f:
            f.write(data['text'])

        chapters_filename = episode_id + '_chapters.json'
        with open(chapters_filename, 'w') as f:
            chapters = data['chapters']

            episode_data = {'chapters': chapters}
            episode_data['episode_thumbnail'] = episode_thumbnail
            episode_data['episode_title'] = episode_title
            episode_data['podcast_title'] = podcast_title

            json.dump(episode_data, f)
            print('transcript saved')

    elif error:
        print("error!")
        return False
