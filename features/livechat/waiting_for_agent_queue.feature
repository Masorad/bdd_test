Feature: when agents are overloaded, customers waits in queue

  @skip
  Scenario: When agents are overloaded, customers waits in queue
    Given brand has maximum sessions per agent se to "1"
    And brand is "online" for chat
    When customer "Ruda Pruda" opens brand page
    And "Ruda Pruda" waits for "1" seconds
    And customer "Ruda Pruda" "expands" chat window
    And customer "Ruda Pruda" fills "Ruda Pruda" into name input
    Then "Ruda Pruda" chat window should show conversation interface

    When customer "Pepa z Depa" opens brand page
    And "Pepa z Depa" waits for "1" seconds
    And customer "Pepa z Depa" "expands" chat window
    And customer "Pepa z Depa" fills "Ruda Pruda" into name input
    Then "Pepa z Depa" should be in waiting queue at "1" posion

    When "Ruda Pruda" ends chat session
    Then "Pepa z Depa" chat window should show conversation interface

