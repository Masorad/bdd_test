Feature: agent can add note to chat message

  Scenario: Agent adds note to customer message
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

    When agent opens chat session
    And agent sends note "Hey boss, I need help!"
    And "agent" waits for "1" seconds
    Then agent should see note "Hey boss, I need help!"
