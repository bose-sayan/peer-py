import logging

console_logger = logging.getLogger("ppy_logger")
console_logger.setLevel(logging.DEBUG)
console_logger.addHandler(logging.StreamHandler())
console_logger.propagate = False
