import boto3
import os
import time

# ec2 = boto3.resource('ec2', region_name = os.environ.get('REGION'))
ec2 = boto3.client('ec2', region_name = os.environ.get('REGION'))

def get_ec2_status():
#    for instance in ec2.instances.all():
    for instance in ec2.run_instances():
        bool_variable = False
        MaxCount=123
        MinCount=123
        for tag in instance.tags:
            if tag['Key'] == "k8s.io/role/master" and tag['Value'] == "1" and instance.state["Code"] == 16:
                bool_variable = True
        if bool_variable == True:
            for tag in instance.tags:
                if tag['Key'] == "Name":
                    print(f"Instance ID:",instance.id, ", Instance Name:", tag['Value'])

get_parameter_from_jenkins = os.environ.get('INTERVAL')

while True:
    get_ec2_status()
    time.sleep(int(get_parameter_from_jenkins))
