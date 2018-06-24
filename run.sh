#!/bin/bash

docker run -it --rm --name project mipsasm python ./mipsasm.py --file $1 
