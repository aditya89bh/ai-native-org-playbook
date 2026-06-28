# Quickstart

This guide gets you from clone to first assessment.

## 1. Install locally

```bash
git clone https://github.com/aditya89bh/ai-native-org-playbook.git
cd ai-native-org-playbook
python -m pip install -e ".[dev]"
```

## 2. Run the tests

```bash
pytest
```

## 3. Score organization readiness

```bash
ai-org-playbook readiness examples/readiness_scores.json
```

## 4. Score a workflow

```bash
ai-org-playbook workflow workflows/specs/customer_onboarding.json
```

## 5. Generate a roadmap

```bash
ai-org-playbook roadmap --readiness-score 3.4 --governance-risk 45
```

## Suggested first use

Start with one department, one workflow, and one or two agent roles. Do not redesign the entire organization in the first pass.
