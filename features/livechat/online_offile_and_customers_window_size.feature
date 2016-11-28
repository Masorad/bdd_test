Feature: basic live chat window

  Scenario Outline: customer opens page of a brand that is "<status>" for chat
    Given brand is "<status>" for chat
    When customer opens brand page
    And "customer" waits for "5" seconds
    Then chat window should be "collapsed"
    And chat window status should be "<status>"

    Examples:
      | status  |
      | offline |
      | online  |

  Scenario Outline: customer expands collapsed "<status>" chat window
    Given brand is "<status>" for chat
    And customer opens brand page
    And "customer" waits for "3" seconds
    When customer "expands" chat window
    And "customer" waits for "3" seconds
    Then chat window should be "expanded"
    And chat window status should be "<status>"

    Examples:
      | status  |
      | offline |
      | online  |

  Scenario Outline: customer collapses expanded "<status>" chat window
    Given brand is "<status>" for chat
    And customer opens brand page
    And "customer" waits for "3" seconds
    And customer "expands" chat window
    And "customer" waits for "3" seconds
    When customer "collapses" chat window
    And "customer" waits for "3" seconds
    Then chat window should be "collapsed"
    And chat window status should be "<status>"

    Examples:
      | status  |
      | offline |
      | online  |

  Scenario Outline: brand goes from "<init_status>" to "<end_status>" for chat when chat window is collapsed
    Given brand is "<init_status>" for chat
    And customer opens brand page
    And "agent" waits for "3" seconds
    When brand goes "<end_status>" for chat
    And "customer" waits for "3" seconds
    Then chat window should be "collapsed"
    And chat window status should be "<end_status>"

    Examples:
      | init_status | end_status |
      | offline     | online     |
      | online      | offline    |

  Scenario Outline: brand goes from "<init_status>" to "<end_status>" for chat when chat window is expanded
    Given brand is "<init_status>" for chat
    And customer opens brand page
    And "agent" waits for "3" seconds
    And customer "expands" chat window
    When brand goes "<end_status>" for chat
    And "customer" waits for "3" seconds
    Then chat window should be "expanded"
    And chat window status should be "<end_status>"

    Examples:
      | init_status | end_status |
      | offline     | online     |
      | online      | offline    |
