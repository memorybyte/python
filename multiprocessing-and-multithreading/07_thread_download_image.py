import threading
import time
import requests

def download(url):
    print(f'Starting download from: {url}')
    response = requests.get(url)
    print(f'Finished downloading from url: {url}, size: {len(response.content)} bytes')

urls = [
    'https://httpbin.org/image/jpeg',
    'https://httpbin.org/image/png',
    'https://httpbin.org/image/svg',
]

threads = []

start = time.time()

for url in urls:
    thread = threading.Thread(
        target=download,
        args=(url, )
    )
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()

print(f'All downloads done in {end - start:.2f} seconds')

