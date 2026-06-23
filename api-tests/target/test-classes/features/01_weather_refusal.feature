Feature: Unsupported Question Refusal

Background:
* url baseUrl

Scenario: Assistant should refuse unsupported questions
Given path 'query'
And header X-User-Region = 'Americas'
And header X-User-Role = 'Employee'
And request
"""
{
  "question": "What is the weather?"
}
"""
When method post
Then status 200
And match response.answer contains 'do not have'
And match response.citations == []