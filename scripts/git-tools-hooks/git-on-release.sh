#!/bin/bash

VERSION=$1
DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
INIT_PATH="$DIR/../../ghostly/__init__.py"

echo "### MUNGING VERSION $VERSION INTO $INIT_PATH"

if [ -z  "$VERSION" ]; then
    echo "VERSION must be specified!"
    exit 1
fi

PY_VERSION=`echo $VERSION | sed -e 's/\./, /g'`

# Replace the version number
sed --in-place -e "s/VERSION = version_info_t(.*)/VERSION = version_info_t($PY_VERSION, '', '')/g" $INIT_PATH

# Ensure we haven't caused some kind of error
python $INIT_PATH

# Check the last commands return code
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

# We're all good, add it to git for the commit
git add $INIT_PATH
