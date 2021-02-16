from pafy import new
from utils.constants import FILE_LOCATION


# download YouTube video in webm format
# id - YouTube id video, HXoj9rOWSO4
# return the file name (title)
def download_webm_file_by_id(id):

    url = 'https://www.youtube.com/watch?v=' + id
    video = new(url)

    bestaudio = video.getbestaudio()
    bestaudio.download(FILE_LOCATION)

    return video.title


if __name__ == "__main__":
    title = download_webm_file_by_id("nzT5YPAIGZA")
    print(title)
