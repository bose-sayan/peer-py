import requests
import bencodepy
import os

from .logger import console_logger
from .helper import byte_str_to_int
from .torrent_file_parser import get_tracker_url, get_info_hash


def connect_to_tracker(decoded_torrent_file):
    tracker_url = get_tracker_url(decoded_torrent_file)
    console_logger.debug(f"tracker_url: {tracker_url}")
    payload = {
        "info_hash": get_info_hash(decoded_torrent_file),
        "peer_id": os.getenv("PEER_ID"),
        "port": int(os.getenv("PORT")),
        "uploaded": 0,
        "downloaded": 0,
        "left": decoded_torrent_file[b"info"][b"length"],
        "compact": 1,
    }
    response = decode_response(send_request(tracker_url, payload))
    return response


def send_request(url, params):
    try:
        response = requests.get(url, params=params)
    except requests.exceptions.RequestException as e:
        console_logger.error(f"Error: {e}")
        return None
    return bencodepy.decode(response.content)


def decode_response(response):
    response_peers = response[b"peers"]
    bin_peers = [response_peers[i : i + 6] for i in range(0, len(response_peers), 6)]
    return {
        "interval": response[b"interval"],
        "peers": [
            {
                "ip": ".".join(str(i) for i in peer[:4]),
                "port": byte_str_to_int(peer[4:]),
            }
            for peer in bin_peers
        ],
    }
