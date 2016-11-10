Feature: messages can be send and delivered

  Scenario: Customer opens chat session and contacts agent
    Given brand is "online" for chat
    And customer opens brand page
    And "customer" waits for "2" seconds
    And customer "expands" chat window
    And "customer" waits for "2" seconds
    And customer fills "Ruda Pruda" into name input
    When customer submits online form in chat window
    Then chat window should show conversation interface
    When customer sends message "Hello, I have a problem. Can you help me?"
    And "agent" waits for "1" seconds
    Then agent should receive chat session from "Ruda Pruda" with "1" message
    When agent opens chat session
    Then agent should receive customers message "Hello, I have a problem. Can you help me?"
    When agent sends message "Hello, whats your problem, sir?"
    And "customer" waits for "1" seconds
    Then customer should receive agents message "Hello, whats your problem, sir?"
