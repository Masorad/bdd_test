Feature: customer can send offline form when brand is offline

  Scenario: customer can send offline form when brand is offline
    Given brand is "offline" for chat
    And brand has offline form "on"
    When customer "Ruda Pruda" opens brand page
    And customer "Ruda Pruda" "expands" chat window
    And customer "Ruda Pruda" starts chat session
    And customer fills offline form "Ruda Pruda", "ruda@pruda.com", "I am so sad, you're offline."
    Then customer "Ruda Pruda" sees information that offline form email has been send.
