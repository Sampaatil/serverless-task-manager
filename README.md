# 🚀 Serverless Task Manager on AWS

A fully serverless web application built using AWS services that allows users to create, view, and delete tasks.

---

## 🧠 Architecture

![Architecture](screenshots/architecture.png)

**Flow:**

User → CloudFront → S3 → API Gateway → Lambda → DynamoDB

---

## ⚙️ Tech Stack

- Amazon S3 (Static Website Hosting)
- Amazon CloudFront (CDN)
- Amazon API Gateway (REST API)
- AWS Lambda (Backend)
- Amazon DynamoDB (Database)
- Amazon CloudWatch (Monitoring)

---

## ✨ Features

- Add Task
- View Tasks
- Delete Task
- Fully Serverless
- Scalable & Cost-efficient

---

## 📸 Screenshots

### Frontend UI
![UI](screenshots/frontend.png)

### DynamoDB
![DB](screenshots/dynamodb.png)

### API Gateway
![API](screenshots/api-gateway.png)

### CloudWatch Logs
![Logs](screenshots/cloudwatch.png)

---

## ⚠️ Challenges & Fixes

### 1. Missing Authentication Token
- Cause: Wrong API endpoint
- Fix: Used `/prod/tasks`

---

### 2. Access Denied (S3)
- Cause: No public access
- Fix: Updated bucket policy

---

### 3. CORS Issues
- Cause: Browser blocked API calls
- Fix: Enabled CORS in API Gateway

---

### 4. CloudFront Cache Issue
- Cause: CDN caching old content
- Fix: Created invalidation (`/*`)

---

## 📈 Learnings

- API Gateway routing
- Lambda event handling
- IAM permissions
- Debugging real AWS errors
- CDN caching behavior

---

## 🚀 Future Improvements

- Add Update Task (PUT API)
- Authentication using Cognito
- CI/CD pipeline
- Custom domain with HTTPS

---

## 🙌 Author

**Samarjeet Patil**

- LinkedIn: https://www.linkedin.com/in/devops-samarjeet/
