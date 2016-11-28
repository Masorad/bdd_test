Feature: Customer sees open chat window by default

  @skip
  Scenario: Customer sees open chat window by default
    Given brand is "online" for chat
    When customer "Ruda Pruda" opens brand page with standalone window
    Then customer "Ruda Pruda" sees expanded chat window