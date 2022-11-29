# rwToT

This code reproduces the result in Meng et al. Advanced Intelligent Systems. "A machine learning approach to real-world time to treatment discontinuation prediction" <br>



## Dependency: 
R 4.1.3 <br>
    library("survival") <br>
    library("timeROC") <br>
    library("Bolstad2") <br>
    library("ROCR")<br>
python 3.9 <br>
    scikit-learn <br>
    keras <br>
    tensorflow<br>



## Structure of code
|_ single_population #single homogeneous population rwToT validation with lightgbm as base learner <br>
    |_delta # test the effect of termination rate<br>
    |_delta_direct_aggregation # test the performance without propagation<br>
    |_simulate_new_feature_example_fixed # test the effect of feature number and example number<br>
    |_simulate_new_noise_example_fixed # test the effect of noise level and example number<br>
    |_simulate_scaling # test the effect of feature scaling<br>
    |_simulation_noisefactor_feature # test the effect of noise level and feature number<br>
|_ single_population_dl #single homogeneous population rwToT validation with deep learning as base learner<br>
    |_delta<br>
    |_delta_direct_aggregation<br>
    |_simulate_new_feature_example_fixed<br>
    |_simulate_new_noise_example_fixed<br>
    |_simulate_scaling<br>
    |_simulation_noisefactor_feature<br>
|_ single_population_linear  #single homogeneous population rwToT validation with linear regression as base learner<br>
    |_delta<br>
    |_delta_direct_aggregation<br>
    |_simulate_new_feature_example_fixed<br>
    |_simulate_new_noise_example_fixed<br>
    |_simulate_scaling<br>
    |_simulation_noisefactor_feature<br>
|_ single_population_svm #single homogeneous population rwToT validation with SVM as base learner<br>
    |_delta<br>
    |_delta_direct_aggregation<br>
    |_simulate_new_feature_example_fixed<br>
    |_simulate_new_noise_example_fixed<br>
    |_simulate_scaling<br>
    |_simulation_noisefactor_feature<br>
|_ two population # two/heterogeneous population rwToT validation with lightGBM as base learner<br>
    |_two_population_delta # test of the differences in termination rate<br>
    |_two_population_example # test the difference in training and test examples<br>
    |_two_population_noise # test the difference in feature noise levels<br>
    |_two_population_scaling # test the difference in feature scaling.<br>


## Running the code
In each of the above subdirectory, there is a base directory and a simulate_all.sh file. <br>
The base directory contains the basic code to test each of the above parameters. <br>
The simulate_all.sh file is the executable that test over a bunch of parameters.<br>
Under each base directory:<br>
|_ simulate.py # simulate the data that follows the distribution to be tested. <br>
    when testing with your own data, please replace the datamatrix from simulate.py<br>
|_ bash.sh # runs through a single cross-validation fold<br>
|_ bash_all.sh # runs through five cross-validations<br>
|_ python3 split.py # split data set into train and test<br>
|_ guanrank.pl # calculate the ranking value in training set<br>
|_ guanrank_time.pl # calculate the future time value for each ranked value<br>
|_ prepare_train.pl # prepare training dataset, test dataset and validation dataset using the estimated future time<br>
|_ train.py # train and interpolate prediction results<br>

 
