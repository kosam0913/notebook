# Table of Contents

1-3. <a href="#introduction">Introduction</a>

4. <a href="#iam--aws-cli">IAM & AWS CLI</a>

5. <a href="#ec2-fundamentals">EC2 Fundadamentals</a>

6. <a href="#cloudfront">CloudFront</a>

7. <a href="#snowball">Snowball</a>

8. <a href="#storage-gateway">Storage Gateway</a>

9. <a href="#elastic-compute-cloud-ec2">Elastic Compute Cloud (EC2)</a>

10. <a href="#elastic-block-store-ebs">Elastic Block Store (EBS)</a>

11. <a href="#elastic-network-interfaces-eni">Elastic Network Interfaces (ENI)</a>

12. <a href="#security-groups">Security Groups</a>

13. <a href="#web-application-firewall-waf">Web Application Firewall (WAF)</a>

14. <a href="#cloudwatch">CloudWatch</a>

15. <a href="#cloudtrail">CloudTrail</a>

16. <a href="#elastic-file-system-efs">Elastic File System (EFS)</a>

17. <a href="#amazon-fsx-for-windows">Amazon FSx for Windows</a>

18. <a href="#amazon-fsx-for-lustre">Amazon FSx for Lustre</a>

19. <a href="#relational-database-service-rds">Relational Database Service (RDS)</a>

20. <a href="#aurora">Aurora</a>

21. <a href="#dynamodb">DynamoDB</a>

22. <a href="#redshift">Redshift</a>

23. <a href="#elasticache">ElastiCache</a>

24. <a href="#route53">Route53</a>

25. <a href="#elastic-load-balancers-elb">Elastic Load Balancers (ELB)</a>

26. <a href="#auto-scaling">Auto Scaling</a>

27. <a href="#virtual-private-cloud-vpc"> Virtual Private Cloud (VPC)</a>

28. <a href="#simple-queuing-service-sqs"> Simple Queuing Service (SQS)</a>

29. <a href="#simple-workflow-service-swf"> Simple Workflow Service (SWF)</a>

30. <a href="#simple-notification-service-sns"> Simple Notification Service (SNS)</a>

31. <a href="#kinesis"> Kinesis </a>

32. <a href="#lambda"> Lambda </a>

33. <a href="#api-gateway"> API Gateway </a>

34. <a href="#cloudformation">CloudFormation </a>

35. <a href="#cloudformation">ElasticBeanstalk</a>

36. <a href="#aws-organizations">AWS Organizations</a>

37. <a href="#miscellaneous">Miscellaneous</a>

---

# AWS Solution Architect Notes

# 1-3 Introduction <a id="introduction"></a>

31% of the market share
Region & Availability Zone (AZ):

- Region: a geographical area (e.g. US East, US West, Asia Pacific)
- Availability Zone (AZ): a physical data center within a region (e.g. us-east-1a, us-east-1b)

# 4. IAM & AWS CLI <a id="iam--aws-cli"></a>

## 4.1 IAM: Identity Access Management

### IAM Entities:

**Users** - any individual end user such as an employee, system architect, CTO, etc.

**Groups** - any collection of similar people with shared permissions such as system administrators, HR employees, finance teams, etc. Each user within their specified group will inherit the permissions set for the group.

**Roles** - any software service that needs to be granted permissions to do its job, e.g- AWS Lambda needing write permissions to S3 or a fleet of EC2 instances needing read permissions from a RDS MySQL database.

**Policies** - the documented rule sets that are applied to grant or limit access. In order for users, groups, or roles to properly set permissions, they use policies. Policies are written in JSON and you can either use custom policies for your specific needs or use the default policies set by AWS.

User / Group / Policy:

- Account + UserGroup + Assigned Policy
- MFA：Multi Factor Authentication (MFA) = password + security device (token)
  - Virtual MFA devices: Google Authenticator, Authy, etc.
  - Universal 2nd Factor (U2F) devices: YubiKey, etc. ( multi user share one device )
  - Hardware Keu fob: AWS Key Fob, etc.

IAM Roles:

- e.g. EC2 Instance Roles, Lamda Function Roles, Roles for Cloud Formation

Security Tools:

- Crednetial Report (Account-level): a report that lists all your account's users and the status of their various credneitials
- Access Advisor (User-level): a tool that shows the service permissions granted to a user and when those services were last accessed

**XHU Notes**: 和 Shotgun Permission 管理思路类似

## 4.2 AWS CLI

Access AWS:

- AWS Management Console (protected by password + MFA)
- AWS Command Line Interface (CLI) (protected by access key)
- AWS SDKs: software development kits (protected by access key)
  Access keys are generated through AWS Console
- CLI alternatives: AWS CloudShell (broswer-based terminal)

```
> aws configure
>> AWS Access Key ID [None]: <your_access_key_id>
>> AWS Secret Access Key [None]: <your_secret_access_key>
>> DEFAULT region name [None]: <your_default_region>
>> Default output format [None]: json
```

**XHU Notes**: Similar to Linux CLI, but with AWS-specific commands

### Best Practices

- Root account is only for account management
- Assign User to Groups, permissions ( policy )to Groups, for better management
- Prgrammatic access via AWS CLI or SDKs, using access keys
- Two tools to audit permissions: IAM Credential Report and IAM Access Advisor

## Summary - IAM & AWS CLI

- Users: mapped to a physical user, has a password for AWS Console
- Groups: contains users only
- Policies: JSON document that outlines permissions for users or groups
- Roles: for EC2 instances or AWS services
- Security: MFA + Password Policy
- AWS CLI: manage your AWS services using the command-line
- AWS SDK: manage your AWS services using a programming language
- Access Keys: access AWS using the CLI or SDK
- Audit: IAM Credential Reports & IAM Access Advisor
