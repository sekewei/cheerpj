#!/bin/sh
set -eu

cd "$(dirname "$0")"

./build.sh
python3 server.py "${1:-8001}"
