import peer_py.torrent_file_parser as tfp
from peer_py.connect_to_tracker import send_request
from peer_py.logger import console_logger

if __name__ == "__main__":
    torrent_file = "./data/debian-12.5.0-amd64-netinst.iso.torrent"
    decoded_torrent_file = tfp.decodeTorrentFile(torrent_file)

    tracker_url = tfp.getTrackerUrl(decoded_torrent_file)
    console_logger.debug(f"tracker_url: {tracker_url}")
    payload = {
        "info_hash": tfp.getInfoHash(decoded_torrent_file),
        "peer_id": "-PC0001-123456789012",
        "port": 6881,
        "uploaded": 0,
        "downloaded": 0,
        "left": decoded_torrent_file[b"info"][b"length"],
        "compact": 1,
    }
    console_logger.debug(f"payload: {payload}")
    response = send_request(tracker_url, payload)
    console_logger.debug(f"response: {response}")
