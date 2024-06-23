import bencodepy
import hashlib
from .logger import console_logger
from .helper import byte_str_to_hex


def parse_torrent_file(torrent_file):
    with open(torrent_file, "rb") as f:
        return bencodepy.decode(f.read())


def get_tracker_url(decoded_torrent_file):
    return decoded_torrent_file[b"announce"].decode("utf-8")


def get_info_hash(decoded_torrent_file):
    info = decoded_torrent_file[b"info"]
    bencodedInfo = bencodepy.encode(info)
    return hashlib.sha1(bencodedInfo).digest()


def get_piece_length(decoded_torrent_file):
    return decoded_torrent_file[b"info"][b"piece length"]


def get_pieces_hashes(decoded_torrent_file):
    pieces = decoded_torrent_file[b"info"][b"pieces"]
    return [byte_str_to_hex(pieces[i : i + 20]) for i in range(0, len(pieces), 20)]
