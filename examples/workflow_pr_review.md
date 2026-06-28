# Example: Pull Request Review Workflow Run

## Workflow

AI-assisted pull request review preparation.

## Agents involved

- Code Review Agent
- Knowledge Agent
- Incident Agent

## Run

1. Agent summarizes the diff and linked issue.
2. Agent retrieves related architecture decisions.
3. Agent suggests missing test cases.
4. Human reviewer checks correctness and risk.
5. Human approves or requests changes.
6. Agent logs review memory and follow-up debt.

## Output

- Review summary
- Test suggestions
- Risk notes
- Review memory update

## Success metric

Lower reviewer load without weakening human code ownership.
