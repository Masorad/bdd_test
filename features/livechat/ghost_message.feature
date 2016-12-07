Feature: agent can see how customer is typing

  Scenario: agent can see how customer is typing
    Given feature "live-chat-v2-send-while-typing" switch is "on"
    And brand is "online" for chat
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
    When customer types message "I'm writing very looong message"
    And "agent" waits for "2" seconds
    Then agent should receive ghost message "I'm writing very looong message"
