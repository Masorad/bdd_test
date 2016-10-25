Feature: agent can add note to chat message

  @skip
  Scenario: livechat_is_typing.feature
    Given agent "Karel" is "online" for chat
    When customer "Ruda Pruda" opens brand page
    And customer "Ruda Pruda" "expands" chat window
    And customer "Ruda Pruda" starts chat session
    And customer sends message "Hello, I have a problem. Can you help me?"
    When agent "Karel" opens chat session
    And agent "Karel" create note for session "Dump user."
    Then agent "Karel" sees note "Dump user."
    And customer "Ruda Pruda" does not sees any note.

