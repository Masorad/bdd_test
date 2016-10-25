Feature: agent can reassign chat to another agent

  Scenario: Agent reassigns chat
    Given agent "Karel" is "online" for chat
    And agent "Josef" is "online" for chat
    When customer "Ruda Pruda" opens brand page
    And customer "Ruda Pruda" "expands" chat window
    And customer "Ruda Pruda" starts chat session
    And customer "Ruda Pruda" sends message "Hello, I have a problem. Can you help me?"
    Then agent "Karel" should receive chat session from "Ruda Pruda"
    When agent "Karel" opens chat session
    And agent "Karel" reassigns chat session to agent "Josef"
    Then agent "Josef" should receive chat session from "Ruda Pruda"
    When agent "Josef" opens chat session
    Then agent "Josef" should receive customers message "Hello, I have a problem. Can you help me?"
