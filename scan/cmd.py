import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-P",
    "--path",
    type=str,
    default=".",
    dest="path",
    metavar="",
    help="Path to scan",
)
parser.add_argument(
    "-M",
    "--mime",
    type=str,
    dest="mime",
    metavar="",
    help="Find file like audio, video or image",
)
