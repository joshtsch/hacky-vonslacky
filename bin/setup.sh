#!/bin/bash

virtualenv .envpy3project

if [[ "$OSTYPE" == "win32" ]] || [[ "$OSTYPE" == "msys" ]] ; then
    source .envpy3project\\Scripts\\activate
else
    source .envpy3project/bin/activate
fi
