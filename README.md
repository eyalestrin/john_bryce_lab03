# Jenkins required plugins:
* Workspace Cleanup
* Pipleline Utility Steps
* Pipleline: Stage View
* Discard Old Build

# Pre-Requirements
1. Create an IAM group, as explained on:  
 https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_create.html
2. Attach the policy **"AmazonEC2ReadOnlyAccess"**, as explained on:  
  https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_attach-policy.html
3. Create an IAM user for programmatic access only, as explained on:  
  https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html  
  Note 1: Add the IAM user to the previously created group.  
  Note 2: Save the **"credentials.csv"** in a secured location  
4. Create **".aws"** folder:  
  **mkdir ~/.aws**  
5. Create the file below on your local Linux machine:  
  **echo "[default]" > ~/.aws/credentials**  
  **echo "aws_access_key_id = <AWS_ACCESS_KEY>" >> ~/.aws/credentials**  
  **echo "aws_secret_access_key = <AWS_SECREST_ACCESS_KEY_ID>" >> ~/.aws/credentials**  
  Note: Replace **<AWS_ACCESS_KEY>** and **<AWS_SECREST_ACCESS_KEY_ID>** with the values from the **"credentials.csv"**  

# Uploading AWS credentials file to Jenkins
1. Login to Jenkin console
2. Follow the instructions below and add a new global credential:  
   https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials  
   Credential type: **Secret file**  
   When asked to choose a file, select the previously created **credentials** file.  
   ID: **credentials**
3. Click OK
