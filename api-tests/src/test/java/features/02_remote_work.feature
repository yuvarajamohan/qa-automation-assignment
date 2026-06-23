Feature: Remote Work Policy

Background:
* url baseUrl

Scenario: Retrieve remote work policy
Given path 'query'
And header X-User-Region = 'Americas'
And header X-User-Role = 'Employee'
And request
"""
{
  "question": "How many days can I work remotely?"
}
"""
When method post
Then status 200
And match response.citations != []