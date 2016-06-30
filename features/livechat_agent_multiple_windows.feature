Feature: livechat status reflected in all agent's browsers

Scenario Outline: "<status>" status for chat is reflected when agent opens second browser
    Given new livechat feature switch is "on"
    And brand is "<status>" for chat
    When agent opens "second" browser
    Then agent should be "<status>" for chat in "second" browser

    Examples:
        | status    |
        | offline   |
        | online    |

Scenario Outline: status for chat is reflected in second browser when agent changes status to "<end_status>" in first browser
    Given new livechat feature switch is "on"
    And brand is "<init_status>" for chat
    And agent opens "second" browser
    When brand goes "<end_status>" for chat
    Then agent should be "<end_status>" for chat in "second" browser

    Examples:
        | init_status   | end_status    |
        | offline       | online        |
        | online        | offline       |

