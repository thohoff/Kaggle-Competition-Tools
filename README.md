# Kaggle-Competition-Tools
A set of tools I developed while doing Kaggle Competitions. Hopefully others will get some use out of this. Some of these are probably outdated and in need of fixing, and most are pretty messy.

## Model management
### Accountant
Accountant is a lightweight tool for managing and keeping track of models and their performance. 
It allows the user to descibe a model in a descriptor file with few lines of python, then a training program can call accountant with that file to start training using the specification. Additionally flags like "evaluate" can be passed such to accountant and potentially affect program in the descriptor file. 
Usually I heavily modify accountant to fit the characteristics of the competition. 

## Models
### Bayesian Optimization for LightGBM
Bayesian Optimization finds good hyperparameters quite effectively. Here I have it implemented for LightGBM. 

### Random Forest Embeddings with LightGBM
Uses the leafs of a random forest as features. Trained by having a random forest predict a completely random objective. 

### Multithreaded Approximate Nearest Neighbors
Uses Spotify's Annoy library to do Approximate Nearest Neighbors, but is uses Multiprocessing to get a speed up.

### Gradient Boosting Additive Models With Pairwise Interactions
From my Interpretable Machine Learning repository. This model looks no further than pairwise interactions, and is more of a tool to find useful patterns in data then getting strong performance. 
