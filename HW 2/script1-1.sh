#!/bin/bash

srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_1 -K 32 -L 2 -P 4 -H 100 -M cnn --lr 0.003 --reg 0.001
srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_1 -K 32 -L 4 -P 4 -H 100 -M cnn --lr 0.003 --reg 0.001
srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_1 -K 32 -L 8 -P 4 -H 100 -M cnn --lr 0.003 --reg 0.001
srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_1 -K 32 -L 16 -P 4 -H 100 -M cnn --lr 0.003 --reg 0.001

srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_1 -K 64 -L 2 -P 4 -H 100 -M cnn --lr 0.003 --reg 0.001
srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_1 -K 64 -L 4 -P 4 -H 100 -M cnn --lr 0.003 --reg 0.001
srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_1 -K 64 -L 8 -P 4 -H 100 -M cnn --lr 0.003 --reg 0.001
srun -c 2 --gres=gpu:1 --pty python -m hw2.experiments run-exp -n cnn_experiment --run-name exp1_1 -K 64 -L 16 -P 4 -H 100 -M cnn --lr 0.003 --reg 0.001
