Feature: livechat unsorted

@draft
Scenario: customer expands collapsed online chat window to see static form
    Given brand is online for chat
    When customer opens brand page
    And customer expands chat window
    Then chat window should show static form for starting new chat

