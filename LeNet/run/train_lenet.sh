#!/usr/bin/env sh
set -e

/home/z840/caffe-tmp/caffe/build/tools/caffe train --solver=../net/lenet_solver.prototxt $@
