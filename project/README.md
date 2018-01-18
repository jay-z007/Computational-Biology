## Phenotypic Prediction from Transcriptomic features

#### Objective:
The aim of this project is to build a model that takes the Salmon
output and predicts the original population and sequencing_center.

The output from Salmon [an RNA-sequence mapping and quantification tool] on
several datasets is provided. The various samples come from different phenotypes; types of
population in this case. 

The project involves Multi-task learning (predicting more than one label at the same time).
Here the population and the sequencing center are the two labels to be predicted simultaneously.

#### Results:
Diverse selection and classification models were used on the given equivalence
classes. Out of all the models, MultiLayer Perceptron Model was able to give highest F-Score of 0.89 
for classifying into different population and sequencing_center. 
During the midway report, MLP classifier gave an F-Score of 0.91 for classifying into different populations.

Please refer to the Final_Report.pdf for details regarding the process and the implementation. 
We also analyzed the results obtained by using different models and parameters the details of which are also mentioned in the report.
