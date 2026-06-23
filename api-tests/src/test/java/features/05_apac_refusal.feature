Feature: APAC Meal Allowance Refusal

Background:
* url baseUrl

Scenario: In-review policy should not surface
Given path 'query'
And header X-User-Region = 'APAC'
And header X-User-Role = 'Employee'
And request
"""
{
  "question": "What is my daily meal allowance?"
}
"""
When method post
Then status 200
And match response.answer contains 'do not have'
And match response.citations == []