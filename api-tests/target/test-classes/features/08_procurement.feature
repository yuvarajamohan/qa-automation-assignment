Feature: Procurement Policy

Background:
* url baseUrl

Scenario: Finance can access procurement thresholds
Given path 'query'
And header X-User-Region = 'Americas'
And header X-User-Role = 'Finance'
And request
"""
{
  "question": "What are procurement approval thresholds?"
}
"""
When method post
Then status 200
And match response.citations != []