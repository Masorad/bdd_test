Feature: messages can be send and delivered

  Scenario: Customer opens chat session and contacts agent
    Given agent "Karel" is "online" for chat
    When customer "Ruda Pruda" opens brand page
    And customer "Ruda Pruda" "expands" chat window
    And customer "Ruda Pruda" starts chat session
    And customer sends message "Hello, I have a problem. Can you help me?"
    Then agent "Karel" should receive chat session from "Ruda Pruda"
    When agent "Karel" opens chat session
    Then agent "Karel" should receive customers message "Hello, I have a problem. Can you help me?"
    When agent "Karel" sends message "Hello, whats your problem, sir?"
    Then customer "Ruda Pruda" should receive agents message "Hello, whats your problem, sir?"
