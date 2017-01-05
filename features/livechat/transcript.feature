Feature: Transcript of the livechat can be sent

  Scenario: Agent can send transcript of the chat session
   Given brand is "online" for chat
    And customer opens brand page
    And "customer" waits for "2" seconds
    And customer "expands" chat window
    And "customer" waits for "2" seconds
    And customer fills "Ruda Pruda" into name input
    When customer submits online form in chat window
    Then chat window should show conversation interface
    When customer sends message "Hello, I have a problem. Can you help me?"
    And agent opens chat session
    And agent clicks on send transcript link
    And agent fills e-mail "ruda.pruda@brandembassy.com"
    And agent clicks on send transcript button
    Then agent sees transcript sent message

  Scenario: customer can send transcript of the chat session
    Given brand is "online" for chat
      And customer opens brand page
      And "customer" waits for "2" seconds
      And customer "expands" chat window
      And "customer" waits for "2" seconds
      And customer fills "Ruda Pruda" into name input
      When customer submits online form in chat window
      Then chat window should show conversation interface
      When customer sends message "Hello, I have a problem. Can you help me?"
      And customer opens transcript form
      And customer fills e-mail "ruda.pruda@brandembassy.com"
      And customer clicks on send button
      Then customer sees successufly sended transcript message
      And customer closes the transcript form
      And customer clicks on end chat button
      And customer clicks on send transcript link
      When customer fills e-mail "ruda.pruda2@brandembassy.com"
      And customer clicks on send button
      Then customer sees successufly sended transcript message

