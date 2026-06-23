Feature: Engineering Policy Access

Background:
* url baseUrl

Scenario: Engineering can access production data policy
Given path 'query'
And header X-User-Region = 'Americas'
And header X-User-Role = 'Engineering'
And request
"""
{
  "question": "How should production data be handled?"
}
"""
When method post
Then status 200
And match response.citations != []