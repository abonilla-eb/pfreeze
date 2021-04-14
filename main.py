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


if __name__ == '__main__':
    packages = []
    if len(sys.argv) == 1:
        with open('requirements.txt') as req:
            [print(line, end='') for line in req.readlines()]
    elif sys.argv[1] == 'dev':
        with open('requirements.txt') as req, open('requirements-dev.txt') as req_dev:
            [print(line, end='') for line in req.readlines()]
            [print(line, end='') for line in req_dev.readlines()]
    elif sys.argv[1] == 'dev-only':
        with open('requirements-dev.txt') as req_dev:
            [print(line, end='') for line in req_dev.readlines()]
    elif sys.argv[1] == 'new':
        with open('requirements.txt') as req, open('requirements-dev.txt') as req_dev:
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
        with open('requirements.txt') as req, open('requirements-dev.txt') as req_dev:
            pkgs = set(req.readlines())
            pkgs.update(req.readlines())
        pkgs.update(get_installed())
        [print(line) for line in pkgs]
