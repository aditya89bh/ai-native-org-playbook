"""Command line interface for the AI Native Organization Playbook."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .agent_roles import AgentRoleSpec, role_operational_depth
from .decision_rights import recommend_decision_level
from .departments import DepartmentSpec, department_complexity
from .maturity import score_capabilities
from .memory_map import recommend_memory_types
from .opportunity import OpportunityFactors, opportunity_band, score_agent_opportunity
from .pilot import PilotCandidate, pilot_band, pilot_score
from .readiness import readiness_band, readiness_score
from .workflows import WorkflowSpec, workflow_agent_surface_area, workflow_governance_load


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


def _readiness(args: argparse.Namespace) -> int:
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    score = readiness_score({key: int(value) for key, value in data.items()})
    print(json.dumps({"score": round(score, 2), "band": readiness_band(score)}, indent=2))
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
    print(json.dumps({"score": score, "band": pilot_band(score)}, indent=2))
    return 0


def _decision_rights(args: argparse.Namespace) -> int:
    level = recommend_decision_level(
        risk=args.risk,
        reversibility=args.reversibility,
        ambiguity=args.ambiguity,
        confidence=args.confidence,
    )
    print(json.dumps({"recommended_decision_right": level}, indent=2))
    return 0


def _department(args: argparse.Namespace) -> int:
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    spec = DepartmentSpec(
        name=str(data["name"]),
        recommended_agents=tuple(data["recommended_agents"]),
        core_workflows=tuple(data["core_workflows"]),
        memory_types=tuple(data["memory_types"]),
        governance_level=str(data["governance_level"]),
        metrics=tuple(data["metrics"]),
    )
    print(json.dumps({"department": spec.name, "complexity": department_complexity(spec)}, indent=2))
    return 0


def _agent_role(args: argparse.Namespace) -> int:
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
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
    print(json.dumps({"agent_role": spec.name, "operational_depth": role_operational_depth(spec)}, indent=2))
    return 0


def _workflow(args: argparse.Namespace) -> int:
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
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
    print(
        json.dumps(
            {
                "workflow": spec.name,
                "agent_surface_area": workflow_agent_surface_area(spec),
                "governance_load": workflow_governance_load(spec),
            },
            indent=2,
        )
    )
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

    readiness = sub.add_parser("readiness", help="score organization readiness from JSON")
    readiness.add_argument("input", help="path to readiness score JSON")
    readiness.set_defaults(func=_readiness)

    pilot = sub.add_parser("pilot", help="score an AI-native pilot candidate")
    pilot.add_argument("--value", type=int, required=True)
    pilot.add_argument("--feasibility", type=int, required=True)
    pilot.add_argument("--risk", type=int, required=True)
    pilot.add_argument("--measurability", type=int, required=True)
    pilot.add_argument("--sponsor-quality", type=int, required=True)
    pilot.set_defaults(func=_pilot)

    decision = sub.add_parser("decision-rights", help="recommend agent decision rights")
    decision.add_argument("--risk", type=int, required=True)
    decision.add_argument("--reversibility", type=int, required=True)
    decision.add_argument("--ambiguity", type=int, required=True)
    decision.add_argument("--confidence", type=int, required=True)
    decision.set_defaults(func=_decision_rights)

    department = sub.add_parser("department", help="score department redesign complexity")
    department.add_argument("input", help="path to department spec JSON")
    department.set_defaults(func=_department)

    role = sub.add_parser("agent-role", help="score agent role operational depth")
    role.add_argument("input", help="path to agent role spec JSON")
    role.set_defaults(func=_agent_role)

    workflow = sub.add_parser("workflow", help="score workflow agent surface area and governance load")
    workflow.add_argument("input", help="path to workflow spec JSON")
    workflow.set_defaults(func=_workflow)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
