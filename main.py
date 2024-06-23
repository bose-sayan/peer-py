from peer_py.connect_to_tracker import connect_to_tracker
from peer_py.torrent_file_parser import parse_torrent_file
from peer_py.logger import console_logger

from dotenv import load_dotenv

if __name__ == "__main__":

    load_dotenv()

    torrent_file = "./data/debian-12.5.0-amd64-netinst.iso.torrent"
    decoded_torrent_file = parse_torrent_file(torrent_file)
    response = connect_to_tracker(decoded_torrent_file)
    console_logger.debug(response)
