import boto3

aws_access_key_id = 'AKIA57WCMSVPOHNN2ZAF'
aws_secret_access_key = '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'

def create_cloudwatch_alarm(instance_id):
    client = boto3.client('cloudwatch', region_name='us-east-1', aws_access_key_id='AKIA57WCMSVPOHNN2ZAF', aws_secret_access_key='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')

    alarm_name = 'High_CPU_Alarm'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    statistic = 'Average'
    comparison_operator = 'GreaterThanThreshold'
    threshold = 80.0
    evaluation_periods = 5
    period = 60
    alarm_description = 'Alarm when CPU exceeds 80% for 5 consecutive minutes'
    alarm_actions = ['arn:aws:sns:us-east-1:961406604638:.fifo']

    response = client.put_metric_alarm(
        AlarmName=alarm_name,
        AlarmDescription=alarm_description,
        ActionsEnabled=True,
        AlarmActions=alarm_actions,
        MetricName=metric_name,
        Namespace=namespace,
        Statistic=statistic,
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': instance_id
            },
        ],
        Period=period,
        EvaluationPeriods=evaluation_periods,
        Threshold=threshold,
        ComparisonOperator=comparison_operator
    )

# Replace 'YOUR_INSTANCE_ID' with the actual EC2 instance ID
create_cloudwatch_alarm('i-0e2ec0307c5a88976')

