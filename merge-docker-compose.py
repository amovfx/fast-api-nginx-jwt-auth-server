import argparse
from pathlib import Path


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('ext', type=str,
                    help='sub extension of docker-compose.yml')
parser.add_argument('--output', metavar='N', type=str, 
                    help='output file')
args = parser.parse_args()


def docker_compose_pattern():
    return f'*/docker-compose.{args.ext}.yml'


def merge_docker_compose(input_files, output_file):
    lines = []
    for input_file in input_files:
        with open(input_file, 'r') as f:
            lines.extend(f.readlines())
        print(f'{input_file} -> {output_file}')
    with open(output_file, 'w') as f:
        for line in lines:
            if line.startswith('#'):
                f.write(line)
            else:
                f.write('  ' + line)

def search_dir():
    return list(Path.cwd().rglob(docker_compose_pattern()))




if __name__ == '__main__':
    args = parser.parse_args()
    print (search_dir())
    output_file = f'./docker-compose.test.{args.ext}.yml'
    merge_docker_compose(search_dir(), output_file)
    
