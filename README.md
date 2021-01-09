# CI

[![Build Status](https://travis-ci.com/cfroehli/clusterizator.svg?branch=master)](https://travis-ci.com/cfroehli/clusterizator)
[![Maintainability](https://api.codeclimate.com/v1/badges/a399a2c8b01b1815a65e/maintainability)](https://codeclimate.com/github/cfroehli/clusterizator/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a399a2c8b01b1815a65e/test_coverage)](https://codeclimate.com/github/cfroehli/clusterizator/test_coverage)

# Build
    python3 -m venv myenv
    . ./myenv/bin/activate
    cd [project_root]
    pip wheel --no-deps -w dist .

# Test
    python3 -m venv myenv
    . ./myenv/bin/activate
    pip install tox-wheel
    cd [project_root]
    tox

# Display coverage
    tox -- --cov-report html
    tox -e cov-server
    open http://localhost:9000/ in a webbrowser

# TODO
    - add proper tests/fixtures
    - try to make an animated version
    - try to use poetry
