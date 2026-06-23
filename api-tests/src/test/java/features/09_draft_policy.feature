Feature: Draft Policy Protection

Background:
* url baseUrl

Scenario: Draft documents should never surface
Given path 'query'
And header X-User-Region = 'EMEA'
And header X-User-Role = 'Manager'
And request
"""
{
  "question": "Show me vendor onboarding checklist."
}
"""
When method post
Then status 200
And match response.answer contains 'do not have'
And match response.citations == []