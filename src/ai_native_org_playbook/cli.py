"""Command line interface for the AI Native Organization Playbook."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .maturity import score_capabilities
from .memory_map import recommend_memory_types
from .opportunity import OpportunityFactors, opportunity_band, score_agent_opportunity


def _score_maturity(args: argparse.Namespace) -> int:
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    score, level = score_capabilities({key: int(value) for key, value in data.items()})
    print(json.dumps({"score": round(score, 2), "level": level.value}, indent=2))
    return 0


def _score_opportunity(args: argparse.Namespace) -> int:
    factors = OpportunityFactors(
        repetition=args.repetition,
        context_load=args.context_load,
        decision_frequency=args.decision_frequency,
        compliance_risk=args.compliance_risk,
        human_judgment_required=args.human_judgment_required,
        data_quality=args.data_quality,
    )
    score = score_agent_opportunity(factors)
    print(json.dumps({"score": score, "band": opportunity_band(score)}, indent=2))
    return 0


def _memory_map(args: argparse.Namespace) -> int:
    memories = recommend_memory_types(args.workflow, args.risk, args.customer_facing)
    print(json.dumps({"workflow": args.workflow, "recommended_memory": memories}, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AI-native organization playbook tools")
    sub = parser.add_subparsers(dest="command", required=True)

    maturity = sub.add_parser("maturity", help="score organization maturity from JSON")
    maturity.add_argument("input", help="path to maturity score JSON")
    maturity.set_defaults(func=_score_maturity)

    opportunity = sub.add_parser("opportunity", help="score a workflow agent opportunity")
    opportunity.add_argument("--repetition", type=int, required=True)
    opportunity.add_argument("--context-load", type=int, required=True)
    opportunity.add_argument("--decision-frequency", type=int, required=True)
    opportunity.add_argument("--compliance-risk", type=int, required=True)
    opportunity.add_argument("--human-judgment-required", type=int, required=True)
    opportunity.add_argument("--data-quality", type=int, required=True)
    opportunity.set_defaults(func=_score_opportunity)

    memory = sub.add_parser("memory-map", help="recommend memory layers for a workflow")
    memory.add_argument("workflow")
    memory.add_argument("--risk", choices=["low", "medium", "high"], required=True)
    memory.add_argument("--customer-facing", action="store_true")
    memory.set_defaults(func=_memory_map)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
