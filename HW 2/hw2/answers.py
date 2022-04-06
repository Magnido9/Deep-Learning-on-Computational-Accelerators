r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers


def part1_arch_hp():
    n_layers = 0  # number of layers (not including output)
    hidden_dims = 0  # number of output dimensions for each hidden layer
    activation = "none"  # activation function to apply after each hidden layer
    out_activation = "none"  # activation function to apply at the output layer
    # TODO: Tweak the MLP architecture hyperparameters.
    # ====== YOUR CODE: ======
    # to fill:
    n_layers = 2 # 2
    hidden_dims = 350 # 350
    activation = "relu" # relu
    out_activation = "softmax" # softmax

    # ========================
    return dict(
        n_layers=n_layers,
        hidden_dims=hidden_dims,
        activation=activation,
        out_activation=out_activation,
    )


def part1_optim_hp():
    import torch.nn
    import torch.nn.functional

    loss_fn = None  # One of the torch.nn losses
    lr, weight_decay, momentum = 0, 0, 0  # Arguments for SGD optimizer
    # TODO:
    #  - Tweak the Optimizer hyperparameters.
    #  - Choose the appropriate loss function for your architecture.
    #    What you returns needs to be a callable, so either an instance of one of the
    #    Loss classes in torch.nn or one of the loss functions from torch.nn.functional.
    # ====== YOUR CODE: ======
    loss_fn = torch.nn.CrossEntropyLoss()
    # to fill:
    lr = 0.003 # 0.00003
    weight_decay = 0.000042 # 0.000001
    momentum = 0.9 # 0.9
    # ========================
    return dict(lr=lr, weight_decay=weight_decay, momentum=momentum, loss_fn=loss_fn)


part1_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part1_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part1_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""


part1_q4 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""
# ==============
# Part 2 answers


def part2_optim_hp():
    import torch.nn
    import torch.nn.functional

    loss_fn = None  # One of the torch.nn losses
    lr, weight_decay, momentum = 0, 0, 0  # Arguments for SGD optimizer
    # TODO:
    #  - Tweak the Optimizer hyperparameters.
    #  - Choose the appropriate loss function for your architecture.
    #    What you returns needs to be a callable, so either an instance of one of the
    #    Loss classes in torch.nn or one of the loss functions from torch.nn.functional.
    # ====== YOUR CODE: ======
    lr=0.025
    weight_decay=0.0030
    momentum=0.8
    loss_fn=torch.nn.CrossEntropyLoss()
    # ========================
    return dict(lr=lr, weight_decay=weight_decay, momentum=momentum, loss_fn=loss_fn)


part2_q1 = r"""
first let's calculate using the formula for the number of parameters in one conv layer- 
$k*(c_in*f^2+1)$
first for the regular residual blocks:
$256*(256*3^2+1)=1180160$
now for the bottleneck block:
$64*(256*1^2+1)*2+64*(64*3^2+1)=70016$
as we can see there is much more parameters without a bottleneck block.

In the convolutional layers we have a floating point operation $2*layer_num_of_params*input_size$ times in each layer, so in total 
it is $total_params*image_size*2$
let's estimate the amount for each of our cases, first for the regular block:
$1180160*image_size*2$, and for the residual bottleneck $70016*image_size*2$.
so basically the amount of floating point operations is  around 15 times more for a regular block
 
Spatially the regular block uses 3x3 convolutions while the bottleneck uses 1x1 convolutions, so the regular block is
wider spatially, meaning it is better in spatially combining parameters in comparison to the bottleneck.
Across the feature map, the 1x1 convolution are better in combining parameters because they only calculate across the
feature map, and that makes the bottleneck blocks better then the regular residual blocks from that prespective.
"""

# ==============

# ==============
# Part 3 answers


part3_q1 = r"""
1)it seems like we got the best results with L=4, I assume thats because our model is overfit(we can see from the train acc),
and L4 probably gives us the least overfit model with our hyperparameters.
2)our model became untrainable in L=16, I assume that is due to the vanishing gradient problem which happens at higher depth
of the cnn.
one way to solve it is using skips to preserve the gradient like we do in a resnet, another way is to add batch normalization
which can also help to prevent the vanishing gradients. 
"""

part3_q2 = r"""
The results seem slightly worse in comparison to the first experiement(in L4 we actually get very close results), and we dont get the vanishing gradient problem this
time, the model is still overfit ( we see that the train acc improves but at some point the test acc stops improving) more
then in the first experiment. 
"""

part3_q3 = r"""
in this experiement we get what seems like our worst results yes, the model seems to be even more overfit then before,
in addition to that, it seems like the vanishing gradient problem returns at L=8, probably because we created again a CNN
that is to deep.
"""

part3_q4 = r"""
this seems like our best results so far, we can see that this time we are able to use deeper networks,
thats thanks to the skips in the resnet, and that is probably the reason that we are able to get better results
in comparison to the previous experiements
"""

part3_q5 = r"""
**Your answer:**
1. We based our model of the Resnet model since it allows us to solve the vanishing gradients problem,
in addition we added a few extra pooling layers, which reduces the amount of features and allows better learning.
Another change we added is to increase the early stopping during the learning in order to let our model to learn for more epochs.
2. as we can see from the results, we got a to around 75% test accuracy, which is better
then the results for experiments 1 which were all around 65% and no more then 68.
in addition we can see that this time we do not get a vanishing gradient. 
"""
# ==============
