#!/bin/sh
set -eu

cd "$(dirname "$0")"

if ! command -v javac >/dev/null 2>&1; then
  echo "Error: javac is required. Install a JDK first." >&2
  exit 1
fi

javac --release 8 MyStack3.java
#jar cfe MyStack3.jar MyStack3 MyStack3.class

echo "Built MyStack3.class"
