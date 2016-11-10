Feature: new livechat feature switch

  Scenario: new livechat feature switch is off
    Given feature "live-chat-v2" switch is "off"
    And user is logged into engager
    Then livechat button is missing


  Scenario: new livechat feature switch is on
    Given feature "live-chat-v2" switch is "on"
    And user is logged into engager
    And "agent" waits for "1" seconds
    When brand goes "offline" for chat
    And "agent" waits for "1" seconds
    And brand goes "online" for chat
    And "agent" waits for "1" seconds
    Then agent should be "online" for chat in "first" browser
