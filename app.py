import boto3

ec2 = boto3.resource('ec2', region_name = 'us-east-1')

for instance in ec2.instances.all():
    bool_variable = False
    for tag in instance.tags:
        if tag['Key'] == "k8s.io/role/master" and tag['Value'] == "1" and instance.state["Code"] == 16:
            bool_variable = True
    if bool_variable == True:
        for tag in instance.tags:
            if tag['Key'] == "Name":
                print(f"Instance ID:",instance.id, ", Instance Name:", tag['Value'])
