#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: MIT-0

# {fact rule=python-sns-set-return-subscription-arn@v1.0 defects=1}
import botocore

def set_return_subscription_noncompliant(self, sqs_arn: str, topic_arn: str):
    session = botocore.session.get_session()
    sns_client = session.create_client('sns', 'us-west-2')
    # Noncompliant: Fails to set the ReturnSubscriptionArn argument to True while returning the subscription ARN.
    sns_client.subscribe(TopicArn=topic_arn, Protocol='sqs',
                         Endpoint=sqs_arn)
# {/fact}
