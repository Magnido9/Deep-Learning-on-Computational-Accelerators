#!/bin/bash

srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp2 -K 32 64 128 -L 3 -P 4 -H 100 -M ycn --lr 0.001 --reg 0.001 --early-stopping 10
srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp2 -K 32 64 128 -L 6 -P 4 -H 100 -M ycn --lr 0.001 --reg 0.001 --early-stopping 10
srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp2 -K 32 64 128 -L 9 -P 4 -H 100 -M ycn --lr 0.001 --reg 0.001 --early-stopping 10
srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp2 -K 32 64 128 -L 12 -P 4 -H 100 -M ycn --lr 0.001 --reg 0.001 --early-stopping 10



