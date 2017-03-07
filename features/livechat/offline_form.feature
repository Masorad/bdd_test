Feature: customer can send offline form when brand is offline

  @skip
  Scenario: customer can send offline form when brand is offline
    Given brand is "offline" for chat
    And customer opens brand page
#    Then chat window should show "offline" form
    When customer "expands" chat window
    And "customer" waits for "1" seconds
    And customer fills offline form "Ruda Pruda", "ruda@pruda.com", "I am so sad you're offline."
#    Then customer "Ruda Pruda" sees information that offline form email has been send.
    And "customer" waits for "1" seconds
