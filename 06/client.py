import argparse
import json
import socket
import threading


def send_urls(urls, socket_server):
    data = "\n".join(urls)
    socket_server.send(data.encode('utf-8'))
    response = socket_server.recv(4096)
    result = json.loads(response.decode('utf-8'))
    print(result)
    socket_server.close()


def main_func(filename):
    print("AAAa")
    num_threads = args.t if args.t is not None else 1
    with open(filename, encoding='utf-8') as file:
        urls = file.read().split()
    chunk_size = len(urls) // num_threads
    threads = []
    for i in range(0, len(urls), 1):
        chunk = urls[i:i + chunk_size]
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('localhost', 7))
            print("Connected to server")
            thread = threading.Thread(target=send_urls, args=(chunk, client_socket))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        print("all doone ")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='File with URLs')
    parser.add_argument('-t', type=int, help='threads')
    args = parser.parse_args()
    main_func(args.file_path)
