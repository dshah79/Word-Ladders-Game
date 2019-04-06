import urllib3


def dowloand():
    http = urllib3.PoolManager()

    r = http.request('GET',
                     "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt",
                     preload_content=False)

    with open("data/words.txt", 'wb') as out:
        data = r.read()
        out.write(data)

    r.release_conn()




