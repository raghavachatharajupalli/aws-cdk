from aws_cdk import (
    aws_ec2 as ec2,
    core as cdk)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class CreateEbcStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #load existing vpc into context
        mvpc = ec2.Vpc.from_lookup(self,'VPC',vpc_name="cdk_demo_vpc")

        #create security group with name
        my_sec_group = ec2.SecurityGroup(self,'SGP',security_group_name="myssecgroup",vpc=mvpc)
        #open port 22 from any ipv4
        my_sec_group.add_ingress_rule(ec2.Peer.any_ipv4(),ec2.Port.tcp(22))

        #create ebs volume
        ebs_vol = ec2.Volume(self,'EBS_VOL',availability_zone='ap-south-1a',size=cdk.Size.gibibytes(1))
