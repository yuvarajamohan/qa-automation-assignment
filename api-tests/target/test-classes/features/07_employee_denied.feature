Feature: Employee Cannot Access Engineering Policy

Background:
* url baseUrl

Scenario: Employee should not see engineering policy
Given path 'query'
And header X-User-Region = 'Americas'
And header X-User-Role = 'Employee'
And request
"""
{
  "question": "How should production data be handled?"
}
"""
When method post
Then status 200
And match response.answer contains 'do not have'
And match response.citations == []