Feature: basic live chat window

Scenario: customer opens page of a brand that is offline for chat
    Given brand is offline for chat
    When customer opens brand page
    Then chat window should be collapsed
    And chat window status should be offline

Scenario: customer expands collapsed offline chat window
    Given brand is offline for chat
    And customer opens brand page
    When customer expands chat window
    Then chat window should be expanded
    And chat window status should be offline

Scenario: customer collapses expanded offline chat window
    Given brand is offline for chat
    And customer opens brand page
    And customer expands chat window
    When customer collapses chat window
    Then chat window should be collapsed
    And chat window status should be offline

@wip
Scenario: customer opens page of a brand that is online for chat
    Given brand is online for chat
    When customer opens brand page
    Then chat window should be collapsed
    And chat window status should be online

@wip
Scenario: customer expands collapsed online chat window
    Given brand is online for chat
    When customer opens brand page
    And customer expands chat window
    Then chat window should be expanded
    And chat window status should be online

@wip
Scenario: customer collapses expanded online chat window
    Given brand is online for chat
    And customer opens brand page
    And customer expands chat window
    When customer collapses chat window
    Then chat window should be collapsed
    And chat window status should be online

Scenario: brand goes from offline to online for chat when chat window is collapsed
    Given brand is offline for chat
    And customer opens brand page
    When brand goes online for chat
    Then chat window should be collapsed
    And chat window status should be online

Scenario: brand goes from online to offline for chat when chat window is collapsed
    Given brand is online for chat
    And customer opens brand page
    When brand goes offline for chat
    Then chat window should be collapsed
    And chat window status should be offline

Scenario: brand goes from offline to online for chat when chat window is expanded
    Given brand is offline for chat
    And customer opens brand page
    And customer expands chat window
    When brand goes online for chat
    Then chat window should be expanded
    And chat window status should be online

Scenario: brand goes from online to offline for chat when chat window is expanded
    Given brand is online for chat
    And customer opens brand page
    And customer expands chat window
    When brand goes offline for chat
    Then chat window should be expanded
    And chat window status should be offline

@wip
Scenario: customer expands collapsed online chat window to see static form
    Given brand is online for chat
    When customer opens brand page
    And customer expands chat window
    Then chat window should show static form for starting new chat

