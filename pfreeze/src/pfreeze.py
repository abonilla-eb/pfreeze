from pip._internal.operations import freeze
import sys


def get_installed():
    return [
        pkg for pkg in freeze.freeze()
        if not any([
            exclude in pkg for exclude
            in ['wheel', 'distribute', 'setuptools', 'pip']
        ])
    ]


def run():
    packages = []
    try:
        req = open('requirements.txt', 'r')
    except FileNotFoundError:
        req = open('requirements.txt', 'w+')
    try:
        req_dev = open('requirements-dev.txt', 'r')
    except FileNotFoundError:
        req_dev = open('requirements-dev.txt', 'w+')

    if len(sys.argv) == 1:
        [print(line, end='') for line in req.readlines()]
    elif sys.argv[1] == 'dev':
        [print(line, end='') for line in req.readlines()]
        [print(line, end='') for line in req_dev.readlines()]
    elif sys.argv[1] == 'dev-only':
        [print(line, end='') for line in req_dev.readlines()]
    elif sys.argv[1] == 'new':
        pkgs = list(req.readlines())
        pkgs.extend(req_dev.readlines())
        pkgs_new = list(get_installed())
        for item in pkgs:
            try:
                pkgs_new.remove(item)
            except ValueError:
                pass
        [print(line) for line in pkgs_new]
    elif sys.argv[1] == 'installed':
        [print(line) for line in get_installed()]
    elif sys.argv[1] == 'all':
        pkgs = set(req.readlines())
        pkgs.update(req.readlines())
        pkgs.update(get_installed())
        [print(line) for line in pkgs]

    req.close()
    req_dev.close()
