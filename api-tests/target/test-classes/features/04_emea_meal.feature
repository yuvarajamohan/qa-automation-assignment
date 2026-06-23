Feature: EMEA Meal Allowance

Background:
* url baseUrl

Scenario: Retrieve EMEA meal allowance
Given path 'query'
And header X-User-Region = 'EMEA'
And header X-User-Role = 'Employee'
And request
"""
{
  "question": "What is my meal allowance?"
}
"""
When method post
Then status 200
And match response.citations != []