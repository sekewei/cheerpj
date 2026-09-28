#!/bin/sh
set -eu

cd "$(dirname "$0")"

if ! command -v javac >/dev/null 2>&1; then
  echo "Error: javac is required. Install a JDK first." >&2
  exit 1
fi

javac MyStack.java
jar cfe MyStack.jar MyStack MyStack.class

echo "Built MyStack.jar"
