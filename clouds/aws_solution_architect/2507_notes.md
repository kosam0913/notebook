# Table of Contents

1. <a href="#introduction-aws-certified-solutions-architect-associate">Introduction - AWS Certified Solutions Architect Associate</a>
2. <a href="#code-slides-download">Code & Slides Download</a>
3. <a href="#getting-started-with-aws">Getting started with AWS</a>
4. <a href="#iam-aws-cli">IAM & AWS CLI</a>
5. <a href="#ec2-fundamentals">EC2 Fundamentals</a>
6. <a href="#ec2-solutions-architect-associate-level">EC2 - Solutions Architect Associate Level</a>
7. <a href="#ec2-instance-storage">EC2 Instance Storage</a>
8. <a href="#high-availability-and-scalability-elb-asg">High Availability and Scalability: ELB & ASG</a>
9. <a href="#aws-fundamentals-rds-aurora-elasticache">AWS Fundamentals: RDS + Aurora + ElastiCache</a>
10. <a href="#route-53">Route 53</a>
11. <a href="#classic-solutions-architecture-discussions">Classic Solutions Architecture Discussions</a>
12. <a href="#amazon-s3-introduction">Amazon S3 Introduction</a>
13. <a href="#advanced-amazon-s3">Advanced Amazon S3</a>
14. <a href="#amazon-s3-security">Amazon S3 Security</a>
15. <a href="#cloudfront-aws-global-accelerator">CloudFront & AWS Global Accelerator</a>
16. <a href="#aws-storage-extras">AWS Storage Extras</a>
17. <a href="#decoupling-applications-sqs-sns-kinesis-active-mq">Decoupling applications: SQS, SNS, Kinesis, Active MQ</a>
18. <a href="#containers-on-aws-ecs-fargate-ecr-eks">Containers on AWS: ECS, Fargate, ECR & EKS</a>
19. <a href="#serverless-overviews-from-a-solution-architect-perspective">Serverless Overviews from a Solution Architect Perspective</a>
20. <a href="#serverless-solution-architecture-discussions">Serverless Solution Architecture Discussions</a>
21. <a href="#databases-in-aws">Databases in AWS</a>
22. <a href="#data-analytics">Data & Analytics</a>
23. <a href="#machine-learning">Machine Learning</a>
24. <a href="#aws-monitoring-audit-cloudwatch-cloudtrail-config">AWS Monitoring & Audit: CloudWatch, CloudTrail & Config</a>
25. <a href="#identity-and-access-management-iam-advanced">Identity and Access Management (IAM) - Advanced</a>
26. <a href="#aws-security-encryption-kms-ssm-parameter-store-shield-waf">AWS Security & Encryption: KMS, SSM Parameter Store, Shield, WAF</a>
27. <a href="#networking-vpc">Networking - VPC</a>
28. <a href="#disaster-recovery-migrations">Disaster Recovery & Migrations</a>
29. <a href="#more-solution-architectures">More Solution Architectures</a>
30. <a href="#other-services">Other Services</a>
31. <a href="#whitepapers-and-architectures-aws-certified-solutions-architect-associate">WhitePapers and Architectures - AWS Certified Solutions Architect Associate</a>
32. <a href="#preparing-for-the-exam-practice-exam-aws-certified-solutions-architect-assoc">Preparing for the Exam + Practice Exam - AWS Certified Solutions Architect Assoc</a>
33. <a href="#congratulations-aws-certified-solutions-architect-associate">Congratulations - AWS Certified Solutions Architect Associate</a>

---

# AWS Solution Architect Notes

# 1. Introduction - AWS Certified Solutions Architect Associate <a id="introduction-aws-certified-solutions-architect-associate"></a>

# 2. Code & Slides Download <a id="code-slides-download"></a>

# 3. Getting started with AWS <a id="getting-started-with-aws"></a>

31% of the market share
Region & Availability Zone (AZ):

- Region: a geographical area (e.g. US East, US West, Asia Pacific)
- Availability Zone (AZ): a physical data center within a region (e.g. us-east-1a, us-east-1b)

# 4. IAM & AWS CLI <a id="iam-aws-cli"></a>

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




# 5. EC2 Fundamentals <a id="ec2-fundamentals"></a>
## 5.1
## 5.2

# 6. EC2 - Solutions Architect Associate Level <a id="ec2-solutions-architect-associate-level"></a>
## 6.1
## 6.2

# 7. EC2 Instance Storage <a id="ec2-instance-storage"></a>
## 7.1
## 7.2

# 8. High Availability and Scalability: ELB & ASG <a id="high-availability-and-scalability-elb-asg"></a>
## 8.1
## 8.2

# 9. AWS Fundamentals: RDS + Aurora + ElastiCache <a id="aws-fundamentals-rds-aurora-elasticache"></a>
## 9.1
## 9.2

# 10. Route 53 <a id="route-53"></a>
## 10.1
## 10.2

# 11. Classic Solutions Architecture Discussions <a id="classic-solutions-architecture-discussions"></a>
## 11.1
## 11.2

# 12. Amazon S3 Introduction <a id="amazon-s3-introduction"></a>
## 12.1
## 12.2

# 13. Advanced Amazon S3 <a id="advanced-amazon-s3"></a>
## 13.1
## 13.2

# 14. Amazon S3 Security <a id="amazon-s3-security"></a>
## 14.1
## 14.2

# 15. CloudFront & AWS Global Accelerator <a id="cloudfront-aws-global-accelerator"></a>
## 15.1
## 15.2

# 16. AWS Storage Extras <a id="aws-storage-extras"></a>
## 16.1
## 16.2

# 17. Decoupling applications: SQS, SNS, Kinesis, Active MQ <a id="decoupling-applications-sqs-sns-kinesis-active-mq"></a>
## 17.1
## 17.2

# 18. Containers on AWS: ECS, Fargate, ECR & EKS <a id="containers-on-aws-ecs-fargate-ecr-eks"></a>
## 18.1
## 18.2

# 19. Serverless Overviews from a Solution Architect Perspective <a id="serverless-overviews-from-a-solution-architect-perspective"></a>
## 19.1
## 19.2

# 20. Serverless Solution Architecture Discussions <a id="serverless-solution-architecture-discussions"></a>
## 20.1
## 20.2

# 21. Databases in AWS <a id="databases-in-aws"></a>
## 21.1
## 21.2

# 22. Data & Analytics <a id="data-analytics"></a>
## 22.1
## 22.2

# 23. Machine Learning <a id="machine-learning"></a>
## 23.1
## 23.2

# 24. AWS Monitoring & Audit: CloudWatch, CloudTrail & Config <a id="aws-monitoring-audit-cloudwatch-cloudtrail-config"></a>
## 24.1
## 24.2

# 25. Identity and Access Management (IAM) - Advanced <a id="identity-and-access-management-iam-advanced"></a>
## 25.1
## 25.2

# 26. AWS Security & Encryption: KMS, SSM Parameter Store, Shield, WAF <a id="aws-security-encryption-kms-ssm-parameter-store-shield-waf"></a>
## 26.1
## 26.2

# 27. Networking - VPC <a id="networking-vpc"></a>
## 27.1
## 27.2

# 28. Disaster Recovery & Migrations <a id="disaster-recovery-migrations"></a>
## 28.1
## 28.2

# 29. More Solution Architectures <a id="more-solution-architectures"></a>
## 29.1
## 29.2

# 30. Other Services <a id="other-services"></a>
## 30.1
## 30.2

# 31. WhitePapers and Architectures - AWS Certified Solutions Architect Associate <a id="whitepapers-and-architectures-aws-certified-solutions-architect-associate"></a>
## 31.1
## 31.2

# 32. Preparing for the Exam + Practice Exam - AWS Certified Solutions Architect Assoc <a id="preparing-for-the-exam-practice-exam-aws-certified-solutions-architect-assoc"></a>
## 32.1
## 32.2

# 33. Congratulations - AWS Certified Solutions Architect Associate <a id="congratulations-aws-certified-solutions-architect-associate"></a>
## 33.1
## 33.2