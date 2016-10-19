Feature: chat session can be opened and closed

  Scenario: customer opens and close chat
    Given agent "Karel" is "online" for chat
    When customer "Ruda Pruda" opens brand page
    And customer "Ruda Pruda" "expands" chat window
    And customer "Ruda Pruda" starts chat session
    Then agent "Karel" should receive chat session from "Ruda Pruda"
    When customer "Ruda Pruda" ends session
    Then customer "Ruda Pruda" should see that chat session is "Closed"
    And agent "Karel" should see that chat session is "Closed".

  Scenario: customer opens chat and agent close chat
    Given agent "Karel" is "online" for chat
    When customer "Ruda Pruda" opens brand page
    And customer "Ruda Pruda" "expands" chat window
    And customer "Ruda Pruda" starts chat session
    Then agent "Karel" should receive chat session from "Ruda Pruda"
    When agent "Karel" ends session
    Then agent "Karel" should see that chat session is "Closed"
    And customer "Ruda Pruda" should see that chat session is "Closed"
