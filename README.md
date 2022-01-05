# InfrastructureConfiguration

This is the Github assets folder for the paper intitled "On the Identification and Learning of Software Configuration Systems: A Case Study on OpenStack Projects".
This paper investigates the files that consitutue the configuration system of OpenStack. This latter is one of the most deployed cloud platform for infrastructure management. The intensive use of configuration artifacts in OpenStack makes it a good case study. To identify the different configuration artifacts and categories in OpenStack, we follow this procedure.

1) we conduct a manual intensive analysis of OpenStack documentation and configruation-related changes to identify the different categories of configruation files. This step results in a card sort, where we manually classify +1.7k files. The link to the card sort is at: 
2) At a first step, we leverage a machine learning model that identifies configuration and non-configuration files. We collect features from the source code of our files by using the Chi-sqaure statistical test to select the most relevent features to each class. Our model achieved an AUC median of 97%
3) We leverage another machine learning model that predicts the configurtion category of a conifguration file. Our model achived a weighted AUC median of 98%
4) We also investigate the minimum amount of requried labeled documents in order to achieve an acceptable performance.  

