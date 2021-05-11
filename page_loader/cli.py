import os
import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='Page saving')
    parser.add_argument(
        '-o', '--output',
        help='output direcotry',
        default=os.getcwd()
    )
    parser.add_argument('path')
    parser.add_argument('url')

    return parser


def parse_args():
    parser = get_parser()
    args = parser.parse_args()
    if os.path.isabs(args.path):
        path = os.path.join(os.getcwd(), args.path)
    else:
        path = args.path

    return (path, args.url)
