#!/bin/bash

set -eou pipefail
IFS=$'\n\t'

if [ $# -eq 0 ]; then
    echo "Usage: $0 <shards>"
    exit 1
fi

shards=$1
    
if [[ ! -d "containers/${shards}" ]] ; then
    mkdir "containers/${shards}"
    mkdir "containers/${shards}/cache"
    mkdir "containers/${shards}/times"
    mkdir "containers/${shards}/outputs"
    echo 0 > "containers/${shards}/times/null.time"
fi

python distribution.py --shards "${shards}" --distribution uniform --container "${shards}" --dataset datasets/purchase/datasetfile --label 0

for j in {0..15}; do
    r=$((${j}*${shards}/5))
    python distribution.py --requests "${r}" --distribution uniform --container "${shards}" --dataset datasets/purchase/datasetfile --label "${r}"
done

