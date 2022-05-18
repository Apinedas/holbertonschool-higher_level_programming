#!/bin/bash
# sets a header variable and send GET
curl -sX GET {$1} -H "X-HolbertonSchool-User-Id: 98"
