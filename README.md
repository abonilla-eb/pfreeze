# Pip freeze filter

Filter and organize pip freeze output using two requirement files for production and development/testing environments, requirements.txt and requirements-dev.txt

## Usage

python -m pfreeze [operation]

- (Default): List only packages in requirements.txt
- dev-only: List only packages in requirements-dev.txt
- dev: List packages in both requirements files
- new: List new packages not in any requirements file
- installed: List all installed packages
- all: List all packages, installed or in any requirements files
