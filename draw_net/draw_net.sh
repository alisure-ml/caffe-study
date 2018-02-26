#!/usr/bin/env sh

set -e

draw_net_path=/home/z840/caffe-tmp/caffe/python
net_file_name=net/lenet.prototxt
img_result_file_name=img/lenet.png

echo "begin draw"
python3 ${draw_net_path}/draw_net.py $net_file_name $img_result_file_name
echo "done"
