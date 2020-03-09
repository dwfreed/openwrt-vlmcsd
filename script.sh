#!/bin/bash
set -e
cd $TRAVIS_BUILD_DIR/sdk/$SDK_DIR
export SDK_DIR=$(basename `pwd`)
export PATH=$TRAVIS_BUILD_DIR/sdk/$SDK_DIR/staging_dir/host/bin:$PATH
pushd staging_dir/toolchain-*
TOOLCHAIN_DIR=$(basename `pwd`)
export PATH=$TRAVIS_BUILD_DIR/sdk/$SDK_DIR/staging_dir/$TOOLCHAIN_DIR/bin:$PATH
popd
./scripts/feeds update packages >/dev/null
make defconfig
make package/vlmcsd/compile V=s
make -j1 V=s package/index
cd $TRAVIS_BUILD_DIR/
