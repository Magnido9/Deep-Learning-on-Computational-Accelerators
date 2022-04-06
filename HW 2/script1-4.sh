#!/bin/bash

srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_4 -K 32 -L 8 -P 4 -H 100 -M resnet --lr 0.003 --reg 0.001 --early-stopping 5
srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_4 -K 32 -L 16 -P 4 -H 100 -M resnet --lr 0.003 --reg 0.001 --early-stopping 5
srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_4 -K 32 -L 32 -P 4 -H 100 -M resnet --lr 0.003 --reg 0.001 --early-stopping 5

srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_4 -K 64 128 256 -L 2 -P 4 -H 100 -M resnet --lr 0.003 --reg 0.001 --early-stopping 5
srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_4 -K 64 128 256 -L 4 -P 4 -H 100 -M resnet --lr 0.003 --reg 0.001 --early-stopping 5
srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_4 -K 64 128 256 -L 8 -P 4 -H 100 -M resnet --lr 0.003 --reg 0.001 --early-stopping 5



