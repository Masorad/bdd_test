Feature: Transcript of the livechat can be sent

  @skip
  Scenario: Agent can send transcript of the chat session
    Given agent "Karel" is "online" for chat
    When customer "Ruda Pruda" opens brand page
    And customer "Ruda Pruda" "expands" chat window
    And customer "Ruda Pruda" starts chat session
    And customer sends message "Hello, I have a problem. Can you help me?"
    And agent clicks on send transcript link
    And agent fills e-mail ruda.pruda@brandembassy.com
    And agent clicks on send trancript button
    Then agent sees transcript sent message

  @skip
  Scenario: customer can send transcript of the chat session
    Given agent "Karel" is "online" for chat
    When customer "Ruda Pruda" opens brand page
    And customer "Ruda Pruda" "expands" chat window
    And customer "Ruda Pruda" starts chat session
    And customer sends message "Hello, I have a problem. Can you help me?"
    And customer opens transcript form
    And customer fills e-mail "ruda.pruda@brandembassy.com"
    And customer clicks on send button
    Then customer see successufly sended transcript message
    When agent "Karel" sends message "Hello, whats your problem, sir?"
    And customer clicks on end chat button
    And customer clicks on send transcript link
    Then customer see transcript form
    When customer fills e-mail "ruda.pruda@brandemabssy.com"
    And customer clicks on send button
    Then customer sees successufly sended transcript message

