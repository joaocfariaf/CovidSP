from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import logging as log
from pathlib import Path
import igraph as ig

import model
from params import *

def cli_parser() -> ArgumentParser:
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.description = "Generate 3-layered family/work/friends graph model."
    parser.add_argument(
        '-nf', '--num_families',
        default=int(BASELINE_POPULATION/AVG_FAMILY_SIZE/BASELINE_SCALE_FACTOR),
        type=int,
        help='The number of families in the model'
    )
    parser.add_argument(
        '-o', '--output',
        type=Path,
        help='Output file path'
    )
    return parser

def main() -> None:
    parser = cli_parser()
    args = parser.parse_args()

    output_path: Path = args.output
    if output_path is None:
        output_path = Path('./model.graphml')
        log.info(f'Using default output path {output_path.absolute()}')
    else:
        if output_path.exists():
            log.warning(f'Will overwrite file {output_path.absolute()}')
        if output_path.is_dir():
            raise RuntimeError(f'Specified output path {output_path.absolute()} is a directory.')

    network = model.generate(vars(args))

    if output_path.is_file():
        log.warning(f'Overwriting file {output_path}')
    with open(output_path.absolute(), 'w') as f:
        ig.write(network, f, format='graphml')

if __name__ == "__main__":
    main()