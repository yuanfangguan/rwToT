# rwToT

This code reproduces the result in Meng et al. Advanced Intelligent Systems. "A machine learning approach to real-world time to treatment discontinuation prediction"



## Dependency: 
R 4.1.3 
python 3.9


## Structure of code
|_ single_population #single homogeneous population rwToT validation with lightgbm as base learner
    |_delta # test the effect of termination rate
    |_delta_direct_aggregation # test the performance without propagation
    |_simulate_new_feature_example_fixed # test the effect of feature number and example number
    |_simulate_new_noise_example_fixed # test the effect of noise level and example number
    |_simulate_scaling # test the effect of feature scaling
    |_simulation_noisefactor_feature # test the effect of noise level and feature number
|_ single_population_dl #single homogeneous population rwToT validation with deep learning as base learner
    |_delta
    |_delta_direct_aggregation
    |_simulate_new_feature_example_fixed
    |_simulate_new_noise_example_fixed
    |_simulate_scaling
    |_simulation_noisefactor_feature
|_ single_population_linear  #single homogeneous population rwToT validation with linear regression as base learner
    |_delta
    |_delta_direct_aggregation
    |_simulate_new_feature_example_fixed
    |_simulate_new_noise_example_fixed
    |_simulate_scaling
    |_simulation_noisefactor_feature
|_ single_population_svm #single homogeneous population rwToT validation with SVM as base learner
    |_delta
    |_delta_direct_aggregation
    |_simulate_new_feature_example_fixed
    |_simulate_new_noise_example_fixed
    |_simulate_scaling
    |_simulation_noisefactor_feature
|_ two population # two/heterogeneous population rwToT validation with lightGBM as base learner
    |_two_population_delta # test of the differences in termination rate
    |_two_population_example # test the difference in training and test examples
    |_two_population_noise # test the difference in feature noise levels
    |_two_population_scaling # test the difference in feature scaling.


## Running the code
In each of the above subdirectory, there is a base directory and a simulate_all.sh file. 
The base directory contains the basic code to test each of the above parameters. 
The simulate_all.sh file is the executable that test over a bunch of parameters.
Under each base directory:
|_ simulate.py # simulate the data that follows the distribution to be tested. 
    when testing with your own data, please replace the datamatrix from simulate.py
|_ bash.sh # runs through a single cross-validation fold
|_ bash_all.sh # runs through five cross-validations
|_ python3 split.py # split data set into train and test
|_ guanrank.pl # calculate the ranking value in training set
|_ guanrank_time.pl # calculate the future time value for each ranked value
|_ prepare_train.pl # prepare training dataset, test dataset and validation dataset using the estimated future time
|_ train.py # train and interpolate prediction results

 
