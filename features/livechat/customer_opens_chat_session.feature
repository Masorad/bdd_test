Feature: livechat customer connects to chat

  Scenario Outline: customer expands "<status>" chat window to see "<status>" form
    Given brand is "<status>" for chat
    And customer opens brand page
    And "customer" waits for "1" seconds
    When customer "expands" chat window
    And "customer" waits for "1" seconds
    Then chat window should show "<status>" form

    Examples:
      | status |
      #| offline   |  # offline form is no longer default behavior
      | online |
