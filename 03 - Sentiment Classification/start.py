import json
from yt_extractor import get_audio_url, get_video_infos
from api_comms import save_transcript


def save_video_sentiments(url):
    video_infos = get_video_infos(url)
    url = get_audio_url(video_infos)
    if url:
        title = video_infos["title"]
        title = title.strip().replace(" ", "_")
        title = "data/" + title
        save_transcript(url, title, sentiment_analysis=True)


if __name__ == "__main__":
    save_video_sentiments(
        "https://www.youtube.com/watch?v=e-kSGNzu0hM&ab_channel=Tom%E2%80%99sGuide")
