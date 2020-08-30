#!/usr/bin/env bash

VERSION=$1

if [[ -z "$VERSION" ]]; then
	echo "WARNING: No version set."
	VERSION="NO-VERSION"
else
	echo "* Version set to $VERSION"
	# Change the version of the project.
	find . -type f -name "*.py" -exec sed -i '' -e 's/{{VERSION}}/'"$VERSION"'/g' {} \;
fi

echo ""
echo "* Building distribution package for knn $VERSION"

python -m pip install --upgrade pip setuptools wheel
python setup.py sdist bdist_wheel

echo ""
echo "* Distribution packages created successfully"
ls -l dist
