import requests
import os


def get_apod():
    K_HDURL="hdurl"
    K_EXPLANATION="explanation"
    K_TITLE="title"
    NASA_KEY = os.getenv("NASA_KEY")
    APOD_KEY="DEMO_KEY" if not NASA_KEY else NASA_KEY
    APOD_URL="https://api.nasa.gov/planetary/apod?api_key=" + APOD_KEY

    r = requests.get(APOD_URL)
    r.raise_for_status()
    jres = r.json()
    imgurl = jres.get(K_HDURL)
    explanation = jres[K_EXPLANATION]
    title = jres[K_TITLE]
    i = requests.get(imgurl)
    i.raise_for_status()
    img = i.content
    return {"image" : i.content, "title" : title, "explanation" : explanation, "imgname":imgurl.split("/")[-1]}

if __name__ == "__main__":
    i = get_apod()
    print(i)

