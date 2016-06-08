Feature: basic live chat window

Scenario Outline: customer opens page of a brand that is "<status>" for chat
    Given brand is "<status>" for chat
    When customer opens brand page
    Then chat window should be "collapsed"
    And chat window status should be "<status>"

    Examples:
        | status    |
        | offline   |
        | online    |

Scenario Outline: customer expands collapsed "<status>" chat window
    Given brand is "<status>" for chat
    And customer opens brand page
    When customer "expands" chat window
    Then chat window should be "expanded"
    And chat window status should be "<status>"

    Examples:
        | status    |
        | offline   |
        | online    |

Scenario Outline: customer collapses expanded "<status>" chat window
    Given brand is "<status>" for chat
    And customer opens brand page
    And customer "expands" chat window
    When customer "collapses" chat window
    Then chat window should be "collapsed"
    And chat window status should be "<status>"

    Examples:
        | status    |
        | offline   |
        | online    |

Scenario Outline: brand goes from "<init_status>" to "<end_status>" for chat when chat window is collapsed
    Given brand is "<init_status>" for chat
    And customer opens brand page
    When brand goes "<end_status>" for chat
    Then chat window should be "collapsed"
    And chat window status should be "<end_status>"

    Examples:
        | init_status   | end_status    |
        | offline       | online        |
        | online        | offline       |

Scenario Outline: brand goes from "<init_status>" to "<end_status>" for chat when chat window is expanded
    Given brand is "<init_status>" for chat
    And customer opens brand page
    And customer "expands" chat window
    When brand goes "<end_status>" for chat
    Then chat window should be "expanded"
    And chat window status should be "<end_status>"

    Examples:
        | init_status   | end_status    |
        | offline       | online        |
        | online        | offline       |

