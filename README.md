# InfrastructureConfiguration

This is the Github assets folder for the paper intitled "On the Identification of Software Configuration Systems: ACase Study on OpenStack Projects".
This paper investigates the files that consitutue the configuration system of OpenStack. This latter is one of the most deployed cloud platform for infrastructure management. The intensive use of configuration artifacts in OpenStack makes it a good case study. To identify the different configuration artifacts and categories in OpenStack, we follow this procedure.

1) we conduct a manual intensive analysis of OpenStack documentation and configruation-related changes to identify the different categories of configruation files. This step results in a card sort, where we manually classify +1.7k files. The link to the card sort is at: 
2) To atomatically identiy the category of each conifguration file, we use machine learning models and feature selection technique to select most relevant features from the documents source code. The link to our model is at:
3) We investigate the impact of the model on different training sample sizes to determine at which point our model achives its best performance.
4) We also investigate the types of features that were selected for each configuration file category.   

