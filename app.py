import boto3
import os
import time

ec2 = boto3.resource('ec2', region_name = os.environ.get('REGION'))
#ec2 = boto3.client('ec2', region_name = os.environ.get('REGION'))

def get_ec2_status():
    for instance in ec2.instances.all():
#    for instance in ec2.run_instances(MinCount=1,MaxCount=123):
        bool_variable = False
        for tag in instance.tags:
            if tag['Key'] == "k8s.io/role/master" and tag['Value'] == "1" and instance.state["Code"] == 16:
                bool_variable = True
        if bool_variable == True:
            for tag in instance.tags:
                if tag['Key'] == "Name":
                    print(f"Instance ID:",instance.id, ", Instance Name:", tag['Value'])

get_parameter_from_jenkins = os.environ.get('INTERVAL')

#region_name = os.environ.get('REGION')
#print(f"Region:",region_name)

while True:
    get_ec2_status()
    time.sleep(int(get_parameter_from_jenkins))
