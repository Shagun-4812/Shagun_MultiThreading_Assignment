import threading
import requests
import time
import sys

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

def concurrent_download(urls):
    threads = []
    start_time = time.time()
    for i, url in enumerate(urls):
        t = threading.Thread(target=download_file, args=(url, f"concurrent_file_{i}.txt"))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    print(f"Concurrent download time: {end_time - start_time:.2f} seconds")

def sequential_download(urls):
    start_time = time.time()
    for i, url in enumerate(urls):
        download_file(url, f"sequential_file_{i}.txt")
    end_time = time.time()
    print(f"Sequential download time: {end_time - start_time:.2f} seconds")

def main():
    if len(sys.argv) < 2:
        print("Usage: python file_downloader.py <input_file.txt> or <url1> <url2> ...")
        return
    
    if sys.argv[1].endswith('.txt'):
        with open(sys.argv[1], 'r') as f:
            urls = [line.strip() for line in f]
    else:
        urls = sys.argv[1:]
    
    print(f"Downloading {len(urls)} files...")
    concurrent_download(urls)
    sequential_download(urls)

if __name__ == "__main__":
    main()