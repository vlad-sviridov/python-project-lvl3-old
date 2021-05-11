import os
import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='Page saving')
    parser.add_argument(
        '-o', '--output',
        type=str,
        help='output direcotry',
        default=os.getcwd(),
    )
    parser.add_argument('url')

    return parser


def parse_args():
    parser = get_parser()
    args = parser.parse_args()
    if os.path.isabs(args.output):
        path = os.path.join(os.getcwd(), args.output)
    else:
        path = args.output
    return (path, args.url)
