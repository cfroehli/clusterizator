# CI

[![Build Status](https://travis-ci.com/cfroehli/clusterizator.svg?branch=master)](https://travis-ci.com/cfroehli/clusterizator)

# Build
    python3 -m venv myenv
    . ./myenv/bin/activate
    cd [project_root] 
    pip wheel .

# Test
    python3 -m venv myenv
    . ./myenv/bin/activate
    pip install tox
    cd [project_root] 
    tox

# TODO
    - add proper tests
    - reorg code a bit
    - try to make an animated version
    - try to use poetry
