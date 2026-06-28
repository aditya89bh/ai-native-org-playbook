"""Command line interface for the AI Native Organization Playbook."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .agent_roles import AgentRoleSpec, role_operational_depth
from .assessment_reports import build_roadmap_report
from .decision_rights import recommend_decision_level
from .departments import DepartmentSpec, department_complexity
from .governance import GovernanceRisk, approval_mode, governance_risk_score
from .maturity import score_capabilities
from .memory_map import recommend_memory_types
from .memory_policy import retention_days, should_require_review
from .opportunity import OpportunityFactors, opportunity_band, score_agent_opportunity
from .pilot import PilotCandidate, pilot_band, pilot_score
from .readiness import readiness_band, readiness_score
from .simulators import SimulatorSpec, simulator_complexity, simulator_readiness_hint
from .workflows import WorkflowSpec, workflow_agent_surface_area, workflow_governance_load


def _load_json(path: str) -> dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("expected a JSON object")
    return data


def _print_json(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2))


def _score_maturity(args: argparse.Namespace) -> int:
    data = _load_json(args.input)
    score, level = score_capabilities({key: int(value) for key, value in data.items()})
    _print_json({"score": round(score, 2), "level": level.value})
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
    _print_json({"score": score, "band": opportunity_band(score)})
    return 0


def _memory_map(args: argparse.Namespace) -> int:
    memories = recommend_memory_types(args.workflow, args.risk, args.customer_facing)
    _print_json({"workflow": args.workflow, "recommended_memory": memories})
    return 0


def _memory_policy(args: argparse.Namespace) -> int:
    days = retention_days(args.tier)
    review = should_require_review(args.tier, args.confidence, args.sensitive)
    _print_json(
        {
            "tier": args.tier,
            "retention_days": days,
            "requires_review": review,
        }
    )
    return 0


def _readiness(args: argparse.Namespace) -> int:
    data = _load_json(args.input)
    score = readiness_score({key: int(value) for key, value in data.items()})
    _print_json({"score": round(score, 2), "band": readiness_band(score)})
    return 0


def _pilot(args: argparse.Namespace) -> int:
    candidate = PilotCandidate(
        value=args.value,
        feasibility=args.feasibility,
        risk=args.risk,
        measurability=args.measurability,
        sponsor_quality=args.sponsor_quality,
    )
    score = pilot_score(candidate)
    _print_json({"score": score, "band": pilot_band(score)})
    return 0


def _decision_rights(args: argparse.Namespace) -> int:
    level = recommend_decision_level(
        risk=args.risk,
        reversibility=args.reversibility,
        ambiguity=args.ambiguity,
        confidence=args.confidence,
    )
    _print_json({"recommended_decision_right": level})
    return 0


def _governance(args: argparse.Namespace) -> int:
    data = _load_json(args.input)
    risk = GovernanceRisk(
        financial_impact=int(data["financial_impact"]),
        customer_impact=int(data["customer_impact"]),
        employee_impact=int(data["employee_impact"]),
        legal_exposure=int(data["legal_exposure"]),
        reversibility=int(data["reversibility"]),
        public_visibility=int(data["public_visibility"]),
    )
    score = governance_risk_score(risk)
    _print_json(
        {
            "action": data.get("action"),
            "risk_score": score,
            "approval_mode": approval_mode(score),
        }
    )
    return 0


def _department(args: argparse.Namespace) -> int:
    data = _load_json(args.input)
    spec = DepartmentSpec(
        name=str(data["name"]),
        recommended_agents=tuple(data["recommended_agents"]),
        core_workflows=tuple(data["core_workflows"]),
        memory_types=tuple(data["memory_types"]),
        governance_level=str(data["governance_level"]),
        metrics=tuple(data["metrics"]),
    )
    _print_json({"department": spec.name, "complexity": department_complexity(spec)})
    return 0


def _agent_role(args: argparse.Namespace) -> int:
    data = _load_json(args.input)
    spec = AgentRoleSpec(
        name=str(data["name"]),
        responsibilities=tuple(data["responsibilities"]),
        inputs=tuple(data["inputs"]),
        outputs=tuple(data["outputs"]),
        permissions=tuple(data["permissions"]),
        memory_scope=tuple(data["memory_scope"]),
        escalation_triggers=tuple(data["escalation_triggers"]),
        evaluation_metrics=tuple(data["evaluation_metrics"]),
        department_fit=tuple(data["department_fit"]),
    )
    _print_json(
        {
            "agent_role": spec.name,
            "operational_depth": role_operational_depth(spec),
        }
    )
    return 0


def _workflow(args: argparse.Namespace) -> int:
    data = _load_json(args.input)
    spec = WorkflowSpec(
        name=str(data["name"]),
        department=str(data["department"]),
        human_steps=tuple(data["human_steps"]),
        agent_steps=tuple(data["agent_steps"]),
        shared_steps=tuple(data["shared_steps"]),
        memory_events=tuple(data["memory_events"]),
        governance_points=tuple(data["governance_points"]),
        metrics=tuple(data["metrics"]),
        risks=tuple(data["risks"]),
    )
    _print_json(
        {
            "workflow": spec.name,
            "agent_surface_area": workflow_agent_surface_area(spec),
            "governance_load": workflow_governance_load(spec),
        }
    )
    return 0


def _simulator(args: argparse.Namespace) -> int:
    data = _load_json(args.input)
    spec = SimulatorSpec(
        name=str(data["name"]),
        organization_type=str(data["organization_type"]),
        departments=tuple(data["departments"]),
        agents=tuple(data["agents"]),
        workflows=tuple(data["workflows"]),
        memory_types=tuple(data["memory_types"]),
        governance_rules=tuple(data["governance_rules"]),
        metrics=tuple(data["metrics"]),
    )
    _print_json(
        {
            "simulator": spec.name,
            "complexity": simulator_complexity(spec),
            "readiness_hint": simulator_readiness_hint(spec),
        }
    )
    return 0


def _roadmap(args: argparse.Namespace) -> int:
    report = build_roadmap_report(args.readiness_score, args.governance_risk)
    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AI-native organization playbook tools")
    sub = parser.add_subparsers(dest="command", required=True)

    maturity = sub.add_parser("maturity", help="score organization maturity from JSON")
    maturity.add_argument("input")
    maturity.set_defaults(func=_score_maturity)

    opportunity = sub.add_parser("opportunity", help="score a workflow agent opportunity")
    opportunity.add_argument("--repetition", type=int, required=True)
    opportunity.add_argument("--context-load", type=int, required=True)
    opportunity.add_argument("--decision-frequency", type=int, required=True)
    opportunity.add_argument("--compliance-risk", type=int, required=True)
    opportunity.add_argument("--human-judgment-required", type=int, required=True)
    opportunity.add_argument("--data-quality", type=int, required=True)
    opportunity.set_defaults(func=_score_opportunity)

    memory = sub.add_parser("memory-map", help="recommend memory layers")
    memory.add_argument("workflow")
    memory.add_argument("--risk", choices=["low", "medium", "high"], required=True)
    memory.add_argument("--customer-facing", action="store_true")
    memory.set_defaults(func=_memory_map)

    memory_policy = sub.add_parser("memory-policy", help="evaluate memory policy")
    memory_policy.add_argument("--tier", required=True)
    memory_policy.add_argument("--confidence", type=float, required=True)
    memory_policy.add_argument("--sensitive", action="store_true")
    memory_policy.set_defaults(func=_memory_policy)

    readiness = sub.add_parser("readiness", help="score organization readiness")
    readiness.add_argument("input")
    readiness.set_defaults(func=_readiness)

    pilot = sub.add_parser("pilot", help="score an AI-native pilot candidate")
    pilot.add_argument("--value", type=int, required=True)
    pilot.add_argument("--feasibility", type=int, required=True)
    pilot.add_argument("--risk", type=int, required=True)
    pilot.add_argument("--measurability", type=int, required=True)
    pilot.add_argument("--sponsor-quality", type=int, required=True)
    pilot.set_defaults(func=_pilot)

    decision = sub.add_parser("decision-rights", help="recommend agent rights")
    decision.add_argument("--risk", type=int, required=True)
    decision.add_argument("--reversibility", type=int, required=True)
    decision.add_argument("--ambiguity", type=int, required=True)
    decision.add_argument("--confidence", type=int, required=True)
    decision.set_defaults(func=_decision_rights)

    governance = sub.add_parser("governance", help="score governance risk")
    governance.add_argument("input")
    governance.set_defaults(func=_governance)

    department = sub.add_parser("department", help="score department complexity")
    department.add_argument("input")
    department.set_defaults(func=_department)

    role = sub.add_parser("agent-role", help="score agent role depth")
    role.add_argument("input")
    role.set_defaults(func=_agent_role)

    workflow = sub.add_parser("workflow", help="score workflow surface area")
    workflow.add_argument("input")
    workflow.set_defaults(func=_workflow)

    simulator = sub.add_parser("simulator", help="score simulator complexity")
    simulator.add_argument("input")
    simulator.set_defaults(func=_simulator)

    roadmap = sub.add_parser("roadmap", help="generate roadmap report")
    roadmap.add_argument("--readiness-score", type=float, required=True)
    roadmap.add_argument("--governance-risk", type=int, required=True)
    roadmap.add_argument("--output")
    roadmap.set_defaults(func=_roadmap)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
