import socket
import json
import threading
from collections import Counter
from queue import Queue
from urllib.request import urlopen
import bs4


def handle_client(client_socket):
    data = client_socket.recv(1024)
    url = data.decode('utf-8')

    response = crawl_url(url)

    client_socket.send(response.encode('utf-8'))
    client_socket.close()


def crawl_url(url):
    with urlopen(url) as page_info:
        page = page_info.read().decode('utf-8')

    soup = bs4.BeautifulSoup(page, 'html.parser')
    text = soup.get_text()
    words = text.split()
    word_count = Counter(words)
    top_k_words = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:K])
    return json.dumps(top_k_words)



def worker():
    while True:
        url = url_queue.get()
        if url is None:
            break
        response = crawl_url(url)
        result_queue.put(response)
        url_queue.task_done()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('localhost', 7))
        server.listen(5)

        print("Сервер готов к приему запросов.")

        for _ in range(workers):
            trhead = threading.Thread(target=worker)
            trhead.start()

        while True:
            client_socket, addr = server.accept()
            print(f"Принято соединение от {addr}")
            data = client_socket.recv(1024)
            url = data.decode('utf-8')
            url_queue.put(url)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Сервер для обкачки URL")
    parser.add_argument("-w", type=int, help="Количество воркеров", required=True)
    parser.add_argument("-k", type=int, help="Топ-K частых слов", required=True)
    args = parser.parse_args()

    K = args.k
    workers = args.w

    url_queue = Queue()
    result_queue = Queue()
    main()
