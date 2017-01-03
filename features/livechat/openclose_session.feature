Feature: chat session can be opened and closed

  Scenario: customer opens and closes the chat
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
    And customer opens chat menu
    And click on close session item
    Then customer sees that chat session is "Closed"
    And agent should see that chat session is "Closed"


  Scenario: customer opens and agent closes the chat
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
    When agent closes the chat session
    Then agent should see that chat session is "Closed"
    And customer sees that chat session is "Closed"


