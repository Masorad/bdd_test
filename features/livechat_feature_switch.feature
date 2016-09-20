Feature: new livechat feature switch

  Scenario: new livechat feature switch is off
    Given new livechat feature switch is "off"
    And user is logged into engager
    Then livechat button is missing


  Scenario: new livechat feature switch is on
    Given new livechat feature switch is "on"
    And brand is "offline" for chat
    And brand goes "online" for chat
    Then agent should be "online" for chat in "first" browser

