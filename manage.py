#!/usr/bin/env python3

import argparse

version = "0.10."

parser = argparse.ArgumentParser()

parser.add_argument("-st",
					"--start",
					help="Start the application",
					action="store_true")

parser.add_argument("--getrules",
					help="Get the current rules",
					action="store_true")

ARGV = parser.parse_args()