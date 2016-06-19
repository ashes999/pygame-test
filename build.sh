#!/bin/sh
rm -rf build
rm -rf dist
pyinstaller --onefile main.py
cp *.png dist
rm -rf build
