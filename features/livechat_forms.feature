Feature: livechat customer connects to chat

  Scenario Outline: customer expands "<status>" chat window to see "<status>" form
    Given new livechat feature switch is "on"
    And brand is "<status>" for chat
    And customer opens brand page
    When customer "expands" chat window
    Then chat window should show "<status>" form

    Examples:
      | status |
      #| offline   |  # offline form is no longer default behavior
      | online |

  Scenario: customer submits online form in chat window
    Given new livechat feature switch is "on"
    And brand is "online" for chat
    And customer opens brand page
    And customer "expands" chat window
    And customer fills in valid name in chat window online form
    When customer submits online form in chat window
    Then chat window should show conversation interface

