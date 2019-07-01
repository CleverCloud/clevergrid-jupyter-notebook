#!/usr/bin/env bash

mkdir workdir

jupyter serverextension enable --py bookstore
jupyter notebook --no-browser --port 8080 --ip=0.0.0.0 --config=jupyter_notebook_config.py --notebook-dir="s3://bucket-notebook/>"
