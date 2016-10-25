Feature: customer can fill custom fields to provide initial info for agent

  Scenario: customer fills email before starting chat session into custom fields
    Given brand has "required" "email" custom field named "Email"
    And agent "Karel" is "online" for chat
    When customer "Ruda Pruda" opens brand page
    And customer "Ruda Pruda" "expands" chat window
    And customer "Ruda Pruda" fills "ruda@pruda.com" into custom field
    And customer "Ruda Pruda" starts chat session
    When agent "Karel" opens chat session
    Then agent "Karel" should see filed custom field "Email" with "ruda@pruda.com"
