# File Finder

## Description

Command line program to find a file meeting criteria in a directory structure.

## Why?/Motivation

I wanted to know the oldest file by date modified in a documents directory that had a lot of subfolders, the batch command seemed painful so decided to write a simpler utility

## Quick Start

1. If you don't have python installed, get it [here](https://www.python.org/downloads/)
2. Clone the files into a local directory
3. Open a command prompt in the directory you cloned to and on windows type `python oldestFile.py <directory>` or on Mac `python3 oldestFile.py <directory>`

## Usage

The program allows you to find either the oldest file or the newest file in the directory. Running with no switches will get the oldest file :

`python oldest_file.py <directory>`

The -n or --newest switch will find the newest file:

`python oldestFile.py <directory> -n` or
`python oldestFile.py <directory> --newest`

The program will report back an error if the directory doesn't exist

## Contributing

### Clone the repo

`git clone http:\\github.com\....`
`cd oldest_file`

### Build/maintain

Install python 3.11 or higher for running the code. VS Code is recommended as an IDE.

### Contribute

If you'd like to contribute fork the repository and submit a pull request with your changes.
