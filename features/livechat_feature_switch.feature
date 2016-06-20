Feature: new livechat feature switch

Scenario: new livechat feature switch is off
    Given new livechat feature switch is "off"
    And brand is "online" for chat
    When customer opens brand page with old chat
    Then old chat window status should be "online"

Scenario: new livechat feature switch is on
    Given new livechat feature switch is "off"
    And brand is "offline" for chat
    And new livechat feature switch is "on"
    And agent refreshes engager browser
    And brand goes "online" for chat
    When customer opens brand page with old chat
    Then old chat window status should be "offline"

