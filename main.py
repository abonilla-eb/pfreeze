from pip._internal.operations import freeze
import sys


# Checks 2 files: requirements.txt and requirements-dev.txt

if __name__ == '__main__':
    packages = []
    if len(sys.argv) == 1:
        # pfreeze: list only packages in requirements.txt
        with open('requirements.txt') as req:
            [print(line, end='') for line in req.readlines()]
    elif sys.argv[1] == 'dev':
        # pfreeze dev: list packages in both requirements files
        with open('requirements.txt') as req, open('requirements-dev.txt') as req_dev:
            [print(line, end='') for line in req.readlines()]
            [print(line, end='') for line in req_dev.readlines()]
    elif sys.argv[1] == 'dev-only':
        # pfreeze dev-only: list only packages in requirements-dev.txt
        with open('requirements-dev.txt') as req_dev:
            [print(line, end='') for line in req_dev.readlines()]
    elif sys.argv[1] == 'new':
        # pfreeze new: list new packages not in any requirements file
        with open('requirements.txt') as req, open('requirements-dev.txt') as req_dev:
            pkgs = list(req.readlines())
            pkgs.append(req_dev.readlines())
        pkgs_new = list(freeze.freeze())
        for item in pkgs:
            try:
                pkgs_new.remove(item)
            except ValueError:
                pass
        [print(line) for line in pkgs_new]
    elif sys.argv[1] == 'all':
        # pfreeze all: list all packages
        [print(line) for line in freeze.freeze()]
