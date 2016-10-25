Feature: agent can see how customer is typing

  @skip
  Scenario: agent can see how customer is typing
    Given livechat feature "send message while customer is typing" switch is "off"
    And agent "Karel" is "online" for chat
    When customer "Ruda Pruda" opens brand page
    And customer "Ruda Pruda" "expands" chat window
    And customer "Ruda Pruda" starts chat session
    And agent "Karel" opens chat session
    Then agent "Karel" should receive chat session from "Ruda Pruda"
    When agent "Karel" opens chat session
    And customer "Ruda Pruda" fills message box with "I am typing..."
    Then agent "Karel" should see that customer is typing
