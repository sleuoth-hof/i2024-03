## Test Plan for Crypto and Stock Suggestion Website

### Tester: Kadyrmamat
### Version: 0.1
### Date: 20.06.2024
### Autotests: GitHub

---

### Introduction

#### 1.1 Purpose
The purpose of this test plan is to define the testing approach, strategy, and scope for the crypto and stock suggestion website using Playwright.

#### 1.2 Scope
This test plan covers the functional and non-functional testing of the crypto and stock suggestion website.

#### 1.3 Objectives
The objectives of this test plan are:
- To ensure the website meets the functional and non-functional requirements specified in the requirements document.
- To identify and report defects in the website.
- To ensure the website is user-friendly and meets usability requirements.
- 
### Test Items
The test items for this test plan are:
- Crypto and stock suggestion website

### Features to be Tested
The features to be tested are:

- Suggestion Accuracy (Buy, Sell, Hold)
- User Interface (Responsiveness and usability)
- Data Visualization (Charts and graphs for suggestions)
- Historical Data (Viewing past suggestions)
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

#### 1. Suggestion Accuracy
**Scenario:** Verify Suggestion Accuracy
- **Given:** New market data is available
- **When:** The algorithm runs
- **Then:** The suggestions (Buy, Sell, Hold) should be compared with market trends for accuracy

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
**Scenario:** View Historical Suggestions
- **Given:** Access to past suggestions
- **When:** I navigate to the history page
- **Then:** I should see a list of past suggestions

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

### Manual Testing of Endpoints

#### 1. GET /main/
**Description:** Fetch the main page
- **Method:** GET
- **URL:** `http://localhost:8000/main/`
- **Expected Result:** HTML content of the main page is returned.

#### 2. GET /news/
**Description:** Fetch the latest market news
- **Method:** GET
- **URL:** `http://localhost:8000/news/`
- **Expected Result:** A JSON response containing the latest market news articles.

Example Response:
```json
{
  "status": "success",
  "data": [
    {
      "title": "Market hits all-time high",
      "content": "The stock market reached an all-time high today with major indices...",
      "timestamp": "2024-06-26T12:00:00Z"
    },
    {
      "title": "Crypto regulations tightening",
      "content": "New regulations on cryptocurrency trading are set to be implemented...",
      "timestamp": "2024-06-26T10:00:00Z"
    }
  ]
}
```

#### 3. POST /llm/
**Description:** Process news data for insights
- **Method:** POST
- **URL:** `http://localhost:8000/llm/`
- **Request Body:**
```json
{
  "news_content": "The stock market reached an all-time high today with major indices..."
}
```
- **Expected Result:** A JSON response with insights generated from the news content.

Example Response:
```json
{
  "status": "success",
  "data": {
    "insights": "The market is showing strong bullish trends..."
  }
}
```

#### 4. GET /stockllm/
**Description:** Get stock recommendations
- **Method:** GET
- **URL:** `http://localhost:8000/stockllm/`
- **Expected Result:** A JSON response with stock recommendations.

Example Response:
```json
{
  "status": "success",
  "data": [
    {
      "stock": "AAPL",
      "suggestion": "Buy",
      "confidence": "High"
    },
    {
      "stock": "TSLA",
      "suggestion": "Hold",
      "confidence": "Medium"
    }
  ]
}
```

### Test Schedule
- **Test plan creation:** 4 hours
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
[chromium] › suggestion-accuracy.spec.js:17:5 › Suggestion › Verify Accuracy
Suggestion Accurate!

[chromium] › ui.spec.js:34:5 › User Interface › Check Responsiveness
Responsive Design Verified!

...

10 passed (2.1m)
```

### Reports
Reports will include detailed test execution results, screenshots of issues, and a summary of defects found and resolved. 
