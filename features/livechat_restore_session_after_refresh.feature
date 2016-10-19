Feature: Livechat window restore chat after browser reload

  Scenario: Restore chat sesion in customers window after browser reload
    And agent "Karel" is "online" for chat
    When customer "Ruda Pruda" opens brand page
    And customer "Ruda Pruda" "expands" chat window
    And agent "Karel" opens chat session
    And customer sends message "Hello, I have a problem. Can you help me?"
    And customer "Ruda Pruda" reloads browser
    Then customer "Ruda Pruda" have open session with last customers message "Hello, I have a problem. Can you help me?"
