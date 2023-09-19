
import requests
from api_secrets import API_KEY_ASSEMBLYAI
from api_secrets import API_KEY_LISTENNOTES
import json
import time


headers = {'authorization': API_KEY_ASSEMBLYAI}
endpoint = "https://api.assemblyai.com/v2/transcript"

listennotes_episode_endpoint = "https://listen-api.listennotes.com/api/v2/episodes"
listennotes_headers = {'X-ListenAPI-Key': API_KEY_LISTENNOTES}

def get_episode_audio_url(episode_id):
    url = listennotes_episode_endpoint + '/' + episode_id
    response = requests.request('GET', url, headers=listennotes_headers)

    data = response.json()
    print(data)








# 96d84944f2744f96ac33357653e5f68e

# start transcribing
# audio_url = response.json()['upload_url']

def transcribe(audio_url, sentiment_analysis):
    transcript_request = {"audio_url": audio_url,
                          "sentiment_analysis": sentiment_analysis}
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


def get_transcription_url(url, sentiment_analysis):
    transcript_id = transcribe(url, sentiment_analysis)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
        print("Waiting 30 seconds")
        time.sleep(30)


def save_transcript(url, title, sentiment_analysis=False):
    data, error = get_transcription_url(url, sentiment_analysis)

    if data:
        text_filename = title + ".txt"
        with open(text_filename, "w") as f:
            f.write(data['text'])

        if sentiment_analysis:
            text_filename = title + "_sentiments.json"
            with open(text_filename, "w") as f:
                sentiments = data["sentiment_analysis_results"]
                json.dump(sentiments, f, indent=4)
        print('Transcription saved!!')
        return True
    elif error:
        print("error", error)
        return False
