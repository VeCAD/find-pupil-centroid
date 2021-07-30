#/bin/bash
# c. Seth Loh

ir_samples=interview-sample.zip

set -e

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    mkdir -p ./test_videos
    curl https://eyescan.fra1.digitaloceanspaces.com/autotrack/test_vids/${ir_samples} -o ./test_videos/${ir_samples} &&
        unzip ./test_videos/${ir_samples} -d test_videos
elif [[ "$OSTYPE" == "darwin"* ]]; then
    mkdir -p ./test_videos
    curl https://eyescan.fra1.digitaloceanspaces.com/autotrack/test_vids/${ir_samples} -o ./test_videos/${ir_samples} &&
        unzip ./test_videos/${ir_samples} -d test_videos
elif [[ "$OSTYPE" == "win32" ]]; then
    :
else
    echo "Unsupported OS"
    exit 1
fi

rm -f ./test_videos/*.zip
