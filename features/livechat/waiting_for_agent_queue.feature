Feature: when agents are overloaded, customers waits in queue

  Scenario: When agents are overloaded, customers waits in queue
    Given brand is "online" for chat
    And brand has maximum sessions per agent se to "1"
    And "customer" waits for "100" seconds

    When customer opens brand page
    And "customer" waits for "2" seconds
    And customer "expands" chat window
    And "customer" waits for "2" seconds
    And customer fills "Ruda Pruda" into name input
    When customer submits online form in chat window
    Then chat window should show conversation interface

    When customer opens brand page
    And "customer" waits for "2" seconds
    And customer "expands" chat window
    And "customer" waits for "2" seconds
    And customer fills "Ruda Pruda" into name input
    When customer submits online form in chat window
    Then chat window should show conversation interface

    When "Ruda Pruda" ends chat session
    Then "Pepa z Depa" chat window should show conversation interface

