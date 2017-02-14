Feature: when agents are overloaded, customers waits in queue

  Scenario: When agents are overloaded, customers waits in queue
    Given brand is "online" for chat
    And agent has no open chat sessions
    And brand has maximum sessions per agent se to "1"

    When "first" customer opens brand page
    And "customer" waits for "2" seconds
    And "first" customer "expands" chat window
    And "customer" waits for "2" seconds
    And "first" customer fills "First Ruda Pruda" into name input
    When "first" customer submits online form in chat window
    Then  "first" chat window should show conversation interface

    When "second" customer opens brand page
    And "customer" waits for "2" seconds
    And "second" customer "expands" chat window
    And "customer" waits for "2" seconds
    And "second" customer fills "First Ruda Pruda" into name input
    When "second" customer submits online form in chat window
    Then "second" chat window should be "1" in queue

    When "first" customer ends chat session
    Then "second" chat window should show conversation interface

