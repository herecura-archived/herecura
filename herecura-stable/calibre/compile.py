#!/usr/bin/env python
import compileall
import sys

args = sys.argv
args.pop(0)
for arg in args:
	compileall.compile_dir(arg+'/', force=True)
