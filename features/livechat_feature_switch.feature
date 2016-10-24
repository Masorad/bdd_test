Feature: new livechat feature switch

  Scenario: new livechat feature switch is off
    Given feature "live-chat-v2" switch is "off"
    And user is logged into engager
    Then livechat button is missing


  Scenario: new livechat feature switch is on
    Given feature "live-chat-v2" switch is "on"
    And user is logged into engager
    When brand goes "offline" for chat
    And brand goes "online" for chat
    Then agent should be "online" for chat in "first" browser
