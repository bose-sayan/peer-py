import bencodepy
import hashlib
from .logger import console_logger


def decodeTorrentFile(torrent_file):
    with open(torrent_file, "rb") as f:
        return bencodepy.decode(f.read())


def getTrackerUrl(decoded_torrent_file):
    return decoded_torrent_file[b"announce"].decode("utf-8")


def getInfoHash(decoded_torrent_file):
    info = decoded_torrent_file[b"info"]
    bencodedInfo = bencodepy.encode(info)
    return hashlib.sha1(bencodedInfo).hexdigest()


def getPieceLength(decoded_torrent_file):
    return decoded_torrent_file[b"info"][b"piece length"]


def getHex(piece):
    return "".join("%02x" % i for i in piece)


def getPiecesHashes(decoded_torrent_file):
    pieces = decoded_torrent_file[b"info"][b"pieces"]
    return [getHex(pieces[i : i + 20]) for i in range(0, len(pieces), 20)]
