r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
1-False, the in sample loss is only dependent on the set we train the data on, thus it cant be estimated by the training set thats not included in the training data
2-False, the part of the data allocated for training can cause for over or under fitting 
3-True, The test set is not a part of the validation or training sets whom are used during the cross validation stage
4-False, Generalization error is the error caused by the fact that we cannot sample all data in the world, the data sets used 
  for cross validation, are still part of the cause for the generalization error, non of the folds add data outside of 
  the sample data that we use for the model  
  """

part1_q2 = r"""
My friend's approach isn't justified he is using the test set to evaluate the hyper parameters,which makes the test set
non objective for when we want to see an actual score that represents the accuracy of the model later.
"""

# ==============
# Part 2 answers

part2_q1 = r"""
**Your answer:**
NO, when we increase the K after a certain point it will only worsen our results, because we increase the amount of items
that we use to classify our item, which will eventually mean that we use to many items, in comparison to their variety,
so that the chances that the k nearest neighbours will classify to the class we need will decrease, this is exactly what we
see in the graph from the previous question, after we increase k beyond 3, it starts to worsen the results.
"""

part2_q2 = r"""
1. Using k-fold CV is better than training the model with the entire train-set and selecting the best model with respect 
to train-set accuracy because it can cause to over-fitting the train-set as we choose the model without comparing to real data.
2. Using k-fold CV is better than training the model with the entire train-set and selecting the best model with respect 
to test-set accuracy because it will be harder to detect over-fitting as we score the models according to the test-set 
and not according to unseen data.
"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
Since we use the loss later with its gradient to optimize the model, since delta is a constant it wont be calculated into
the optimization result later. We only want it to be above 0 so that we will make sure to give worse score to wrong predictions.
"""

part3_q2 = r"""
It seems that the model is learning from the location of the white pixels, and the errors seem to stem from shapes that are
very similar, probably because they have similar placing of the pixels to the correct number images.
The linear model learns from the location of the white pixels.
KNN is very similar in the way that it trains also according to the location of the white pixels and its similarity to 
other results.
"""

part3_q3 = r"""
1.It seems like the learning rate we chose might be too high, since our graph has a few points where it has a drastic 
incline or decline in comparison to the rest of the graph, which probably happens because the learning rate is to high.
Which causes a change that's to high.
2.It seems the model is slightly better in the training set then the validation,which insinuates that the model
is slightly overfit.
"""

# ==============

# ==============
# Part 4 answers

part4_q1 = r"""
The ideal pattern to see in a residual plot is a horizontal line at x=0, where the dots are the closest to the line.
as you can see from our graph, it is mostly surrounding the line, even though there are a few odd dots that 
represent mistakes that the model makes, I would say that our model makes a decent prediction, but it does miss on some
spots. On the top 5 feature's graphs you can see that the dots dont really follow the horizontal line, and there are many odd dots,
which shows the inaccuracy there in comparison to the last graph of our model.  

"""

part4_q2 = r"""
1.Yes, we use the non linear features, in aspiration to create a linear model, the non linear features actually use us
to form a linear model.
2.Yes, for every function there is some form of non linear functions that applying them will allow us to negate the non 
linearity of the function.
3.No, the decison boundry will be hyperplane in relation to the non linear features which means he will not be linear in general
"""

part4_q3 = r"""
1. Because it gives us a larger and more variant range of divisions for the given set,better then what we recieve from a linear lambda
2. We use 3 folds, the degree range's size is 3 and the lambda range's size is 20 so in total 3*3*20=180
"""

# ==============
