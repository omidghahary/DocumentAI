Development Rules

Always write tests first.
* Prefer focused tests over exhaustive test combinations.
* Test observable behavior rather than implementation details.
* Once the main behavioral contract of a feature is covered and the test suite is green, move to the next feature unless additional boundary testing has meaningful regression value.

Use Mock for external services.

One feature → one commit.

One milestone → one tag.

No direct dependency between modules.

Pipeline orchestrates only.

Business logic stays inside components.

