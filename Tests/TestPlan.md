## Test Plan for Crypto and Stock Price Prediction Website

### Tester: Kadyrmamat
### Version: 0.1
### Date: 20.06.2024
### Autotests: GitHub

---

### Introduction

#### 1.1 Purpose
The purpose of this test plan is to define the testing approach, strategy, and scope for the crypto and stock price prediction website using Django and React.js.

#### 1.2 Scope
This test plan covers the functional and non-functional testing of the crypto and stock price prediction website.

#### 1.3 Objectives
The objectives of this test plan are:
- To ensure the website meets the functional and non-functional requirements specified in the requirements document.
- To identify and report defects in the website.
- To ensure the website is user-friendly and meets usability requirements.
- To ensure the website is reliable, scalable, and secure.

### Test Items
The test items for this test plan are:
- Crypto and stock price prediction website

### Features to be Tested
The features to be tested are:

- Prediction Accuracy
- User Interface (Responsiveness and usability)
- Data Visualization (Charts and graphs for predictions)
- Historical Data (Viewing past predictions and actual outcomes)
- User Profile Management (Updating user information)
- Security (Protection against common vulnerabilities)

### Test Environment
The test environment will consist of the following:

#### Hardware:
- Desktop computers with Windows 10 operating system and at least 8 GB of RAM

#### Software:
- Google Chrome, Mozilla Firefox, and Microsoft Edge web browsers
- Bug Tracking Tool: JIRA or Bugzilla
- Test Management Tool: Azure DevOps
- Testing Framework: Playwright
- IDE: Visual Studio Code

#### Network:
- Local area network (LAN) with a minimum bandwidth of 100Mbps

### Test Cases

#### 1. Prediction Accuracy
**Scenario:** Verify Prediction Accuracy
- **Given:** New market data is available
- **When:** The algorithm runs
- **Then:** The predictions should be compared with actual outcomes for accuracy

#### 2. User Interface
**Scenario:** Check Responsiveness
- **Given:** Various devices (desktop, tablet, mobile)
- **When:** I access the website
- **Then:** The layout should adjust appropriately for each device

#### 3. Data Visualization
**Scenario:** View Charts and Graphs
- **Given:** Historical and current market data
- **When:** I view the dashboard
- **Then:** The data should be displayed in interactive charts and graphs

#### 4. Historical Data
**Scenario:** View Historical Predictions
- **Given:** Access to past predictions
- **When:** I navigate to the history page
- **Then:** I should see a list of past predictions and their actual outcomes

#### 5. User Profile Management
**Scenario:** Update Profile
- **Given:** `http://localhost:8000/profile`
- **When:** I change my personal information
- **And:** I click on the 'Save' button
- **Then:** My profile should be updated successfully

#### 6. Security
**Scenario:** SQL Injection Test
- **Given:** Input fields across the site
- **When:** I attempt to inject SQL commands
- **Then:** The system should prevent SQL injection and display an error message

### Test Schedule
- **Test plan creation:** 1 day
- **Test case creation:** 2 days
- **Test execution (functional, performance, security testing):** 3 days
- **Defect management:** 2 days
- **Report:** 1 day
- **Acceptance testing:** 1 week

### Test Deliverables
- Test Plan Document
- Test Cases
- Test Execution Reports
- Defect Logs
- Final Test Summary Report

### Logs
Example:
```
Running 10 tests using 2 workers
[chromium] › prediction-accuracy.spec.js:17:5 › Prediction › Verify Accuracy
Prediction Accurate!

[chromium] › ui.spec.js:34:5 › User Interface › Check Responsiveness
Responsive Design Verified!

...

10 passed (2.1m)
```

### Reports
Reports will include detailed test execution results, screenshots of issues, and a summary of defects found and resolved.
