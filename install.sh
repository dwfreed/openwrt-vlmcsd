#!/bin/bash
set -e
mkdir -p $TRAVIS_BUILD_DIR/cache ; cd $TRAVIS_BUILD_DIR/cache
wget -c $SDK_URL
mkdir -p $TRAVIS_BUILD_DIR/sdk ; cd $TRAVIS_BUILD_DIR/sdk
export FILE=$TRAVIS_BUILD_DIR/cache/$(basename $SDK_URL)
tar xf $FILE
SDK_DIR="openwrt-sdk-*"
cd $TRAVIS_BUILD_DIR/sdk/$SDK_DIR
patch -Np1 < $TRAVIS_BUILD_DIR/padding.patch
"echo 'untrusted comment: usign key of Doug Freed' > key-build"
echo "$SIGNING_KEY" >> key-build
mkdir package/vlmcsd
ln -s $TRAVIS_BUILD_DIR/Makefile package/vlmcsd/
ln -s $TRAVIS_BUILD_DIR/files package/vlmcsd/
