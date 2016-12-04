"""Convert txt file containing TOS to json file."""

import argparse
import json
import os


def main(args):
    basename = os.path.basename(args.textfile)
    name, _ = os.path.splitext(basename)
    
    with open(args.textfile, 'r') as f:
        txt = f.read()
    
    data = {'label': args.rating, 'text': txt}
    data['url'] = args.url if args.url else ''
    
    with open('{}.{}'.format(name, 'json'), 'w') as f:
        json.dump(data, f, indent=4)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("textfile", type=str, help="File to containing TOS.")
    parser.add_argument("--rating", type=str, help="TOSDR rating associated "
                        "with the TOS text. Options={'A', 'B', 'C', 'D', E'}")
    parser.add_argument("--url", type=str, help="URL to the webpage containing "
                        "the TOS.")
    return parser.parse_args()

if __name__ == '__main__':
    args = cli()
    main(args)
