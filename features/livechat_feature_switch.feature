Feature: new livechat feature switch

@draft
Scenario Outline: new livechat feature switch is <new_chat_state>
    Given new livechat feature switch is <new_chat_feature_state>
    And brand is offline for chat
    And customer opens brand page with old chat
    When brand goes online for chat
    Then old chat window should be <final_old_chat_status>

    Examples:
        | new_chat_feature_state    | final_old_chat_status |
        | off                       | online                |
        | on                        | offline               |


