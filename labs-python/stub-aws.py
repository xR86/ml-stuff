import boto3

# aws ec2 describe-instances

print 'boto3 imported'
ec2 = boto3.resource('ec2')


print 'finding instances'
instance_list = ec2.instances.all()
print instance_list

print 'enumerating ec2'
for instance in instance_list:
    print '...'
    print instance, instance.state

'''
for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    print(status)
'''

