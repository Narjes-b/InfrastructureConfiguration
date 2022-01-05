# InfrastructureConfiguration

This is the Github assets folder for the paper intitled "On the Identification and Learning of Software Configuration Systems: A Case Study on OpenStack Projects".
This paper investigates the files that consitutue the configuration system of OpenStack. This latter is one of the most deployed cloud platform for infrastructure management. The intensive use of configuration artifacts in OpenStack makes it a good case study. To identify the different configuration artifacts and categories in OpenStack, we follow this procedure.

1) we conduct a manual intensive analysis of OpenStack documentation and configruation-related changes to identify the different categories of configruation files. This step results in a [``card sort``](https://github.com/Narjes-b/InfrastructureConfiguration/blob/main/Data/Card%20Sort.csv), where we manually classify +1.7k files. 
2) At a first step, we leverage a machine learning model that identifies configuration and non-configuration files. We collect features from the source code of our files by using the Chi-sqaure statistical test to select the most relevent features to each class. Our [``model``](https://github.com/Narjes-b/InfrastructureConfiguration/blob/main/Models/Model1-Configuration_Non-configuration.sav) achieved an AUC median of 97%
3) We leverage another machine learning model that predicts the configurtion category of a conifguration file. Our [``model``](https://github.com/Narjes-b/InfrastructureConfiguration/blob/main/Models/Model2-ConfigurationCategories.sav) achived a weighted AUC median of 98%
4) We also investigate the minimum amount of requried labeled documents in order to achieve an acceptable performance.  

To use our model on new data, type this code. 

    # load the model from disk
    loaded_model = pickle.load(open(ModelPath, 'rb'))
    texts = [
        "[DEFAULT] internal_service_availability_zone = internal Default availability zone for compute services. This option determines the default availability zone for 'nova-compute' # services, which will be used if the service(s) do not belong to aggregates default_availability_zone = nova #default_schedule_zone = <None> #password_length = 12 instance_usage_audit_period = month use_rootwrap_daemon = false"]
    text_features = vectorizer.transform(texts)
    print(text_features)
    predictions = loaded_model.predict(text_features)
    print(predictions)
    # for multiple texts
    for text, predicted in zip(texts, predictions):
       print('"{}"'.format(text))
       print("  - Predicted as: '{}'".format(predicted))
       print("")
    


Result:

"[DEFAULT] internal_service_availability_zone = internal Default availability zone for compute services. This option determines the default availability zone for 'nova-compute' # services, which will be used if the service(s) do not belong to aggregates default_availability_zone = nova #default_schedule_zone = <None> #password_length = 12 instance_usage_audit_period = month use_rootwrap_daemon = false"
  - Predicted as: 'Conf-Externals'
