#!/bin/bash

function cleanup {
  rm -rf temp
}

set -e

video=$1

if [ -z "\"$video\"" ]; then
  echo "error: must supply a video to be converted!"
  exit 1
fi

echo "converting video \`$video\`"

if [ -d "temp" ]; then
  echo "error: temp directory already exists!"
  exit 1
fi

mkdir temp

echo 'converting video to frames...'
if ! ffmpeg -i "$video" temp/frame%04d.png ; then
  echo "error: converting video to frames failed"
  cleanup
  exit 1
fi

echo 'converting frames to gif...'
if ! gifski -o output.gif temp/frame*.png ; then
  echo "error: converting frames to gif failed"
  cleanup
  exit 1
fi

cleanup

echo 'gif created! `output.gif`'
exit 0
