#!/bin/bash
# prints allowed HTTP methods
curl -sI {$1} | grep Allow | cut -d" " -f2-
