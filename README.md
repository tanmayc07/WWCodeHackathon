# WWCodeHackathon
# Women Who Code Mission: Predictable hackathon.
## Mission: Predictable A Virtual Machine Learning Hackathon to Battle Covid-19

# Team No. 18 -  Bits N’ Bytes

# COVID-19/SARS B-cell Epitope Prediction
## A simple dataset for epitope prediction used in vaccine development

# Introduction about Dataset

Due to spread of COVID-19, vaccine development is being demanded as soon as possible. Despite the importance of data analysis in vaccine development, there are not many simple data sets that data analysts can handle. The B-cell epitope predictions covered by in this dataset, is one of the key research topics in vaccine development. This dataset was developed during the research process and the data contained in it was obtained from [IEDB](<https://www.iedb.org/>) and [UniProt](<https://www.uniprot.org/>). And predicting of epitope regions is beneficial for the design and development of vaccines aimed to induce antigen-specific antibody production. This dataset has 14387 number of rows for all combinations of 14362 peptides and 757 proteins.

|Column name|Description|
|:----|:----|
|parent_protein_id|parent protein ID|
|protein_seq|parent protein sequence|
|start_position|start position of peptide|
|end_position|end position of peptide|
|peptide_seq|peptide sequence|
|chou_fasman|peptide feature, β turn|
|emini|peptide feature, relative surface accessibility|
|kolaskar_tongaonkar|peptide feature, antigenicity|
|parker|peptide feature, hydrophobicity|
|isoelectric_point|protein feature|
|aromacity|protein feature|
|hydrophobicity|protein feature|
|stability|protein feature|
|target|antibody valence (target value)|

# Relevant Papers

[Epitope Prediction of Antigen Protein using Attention-Based LSTM Network (2020, bioRxiv)](<https://www.biorxiv.org/content/10.1101/2020.07.27.224121v1>)

# Inspiration

Automated methods for B-cell epitope prediction. Machine learning helps rapid vaccine development.

##### The csv file input_bcell.csv for the dataset of this project can be downloaded from [here](<https://www.kaggle.com/futurecorporation/epitope-prediction>)
