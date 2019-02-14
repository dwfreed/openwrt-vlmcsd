#!/bin/bash
# Deploy binaries built with travis-ci to GitHub Pages,
# where they can be accessed by OpenWrt opkg directly
cd /tmp/
git clone https://${USER}:${TOKEN}@github.com/${USER}/${REPO}.git --branch gh-pages --single-branch gh-pages > /dev/null 2>&1 || exit 1
cd gh-pages || exit 1
git config user.name "Doug Freed"
git config user.email "dwfreed@mtu.edu"
mkdir -p $OSVER
pushd $OSVER
ARCH=$(basename $TRAVIS_BUILD_DIR/sdk/$SDK_DIR/bin/packages/*)
rm ${ARCH}/base/*.ipk
cp -r $TRAVIS_BUILD_DIR/sdk/$SDK_DIR/bin/packages/* .
rm -r ${ARCH}/{luci,packages,routing,telephony}
cat > ${ARCH}/index.html <<EOF
<html><body><pre>
echo "src/gz openwrt-vlmcsd http://${USER}.github.io/${REPO}/${OSVER}/${ARCH}/base" >> /etc/opkg.conf
opkg update
opkg install ${PACKAGE}
</pre></body></html>
EOF
DATE=$(date "+%Y-%m-%d")
cat > ${ARCH}/README.md <<EOF
OpenWrt repository for ${PACKAGE}
========
Binaries built from this repository on $DATE can be downloaded from http://${USER}.github.io/${REPO}/.
To install the ${PACKAGE} package, run
\`\`\`
echo "src/gz openwrt-vlmcsd http://${USER}.github.io/${REPO}/${OSVER}/${ARCH}/base" >> /etc/opkg.conf
opkg update
opkg install ${PACKAGE}
\`\`\`
EOF
git add -A
popd
git pull origin gh-pages > /dev/null 2>&1 || exit 1
git commit -a -m "Deploy Travis build $TRAVIS_BUILD_NUMBER for $OSVER $ARCH to gh-pages"
#git push -fq origin gh-pages:gh-pages > /dev/null 2>&1 || exit 1
while ! git push origin gh-pages > /dev/null 2>&1; do
	git pull origin gh-pages > /dev/null 2>&1 || exit 1
done
#git push -f origin gh-pages:gh-pages
echo "Uploaded files to gh-pages"
echo
cd -
