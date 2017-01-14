Feature: customer can switch between views

  Scenario: Agent switches between views and see posts in these
    Given user is logged into engager
    Then agent should see view with name "View with 3 posts"
    Then agent should see view with name "View with 6 posts"
    Then view with name "View with 3 posts" is "not active"
    Then view with name "View with 6 posts" is "not active"
    When agent clicks on view "View with 3 posts"
    Then agent should see "3" items in list of posts
    Then view with name "View with 3 posts" is "active"
    When agent clicks on view "View with 6 posts"
    Then agent should see "6" items in list of posts
    Then view with name "View with 6 posts" is "active"

