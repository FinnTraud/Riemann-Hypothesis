"""
experiment.py — Reproducible experiment logbook for RH research.

Each experiment = {hypothesis, method, parameters, result, conclusion, time}.
Stored as JSON (machine-readable) AND Markdown (human-readable) in kb/experiments/.
Goal: traceable collaboration (e.g. with a math professor).
"""
import os, json, time, hashlib

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "experiments")
os.makedirs(DIR, exist_ok=True)
LOG = os.path.join(DIR, "logbook.jsonl")

def log_experiment(hypothesis, method, params, result, conclusion="", tags=None):
    """Stores an experiment reproducibly. params/result as JSON-serializable dicts."""
    ts = time.strftime("%Y-%m-%dT%H:%M:%S")
    payload = {"hypothesis": hypothesis, "method": method, "params": params,
               "result": result, "conclusion": conclusion, "tags": tags or [],
               "time": ts}
    eid = "exp-" + hashlib.sha1(json.dumps(payload, sort_keys=True, default=str).encode()).hexdigest()[:10]
    payload["id"] = eid
    # append JSONL
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False, default=str) + "\n")
    # single Markdown file
    md = _to_md(payload)
    with open(os.path.join(DIR, eid + ".md"), "w", encoding="utf-8") as f:
        f.write(md)
    return {"id": eid, "saved": True, "markdown": os.path.join(DIR, eid + ".md")}

def _to_md(p):
    return (f"# Experiment {p['id']}\n\n"
            f"- **Time:** {p['time']}\n"
            f"- **Tags:** {', '.join(p['tags']) or '—'}\n\n"
            f"## Hypothesis\n{p['hypothesis']}\n\n"
            f"## Method\n{p['method']}\n\n"
            f"## Parameters\n```json\n{json.dumps(p['params'], ensure_ascii=False, indent=2, default=str)}\n```\n\n"
            f"## Result\n```json\n{json.dumps(p['result'], ensure_ascii=False, indent=2, default=str)}\n```\n\n"
            f"## Conclusion\n{p['conclusion'] or '(open)'}\n\n"
            f"> Note: numerical results are evidence, not proof (see docs/35).\n")

def list_experiments():
    if not os.path.exists(LOG):
        return {"count": 0, "experiments": []}
    exps = [json.loads(l) for l in open(LOG, encoding="utf-8") if l.strip()]
    return {"count": len(exps),
            "experiments": [{"id": e["id"], "time": e["time"],
                             "hypothesis": e["hypothesis"][:90], "tags": e["tags"]}
                            for e in exps]}

def get_experiment(eid):
    if not os.path.exists(LOG):
        return {"error": "no logbook"}
    for l in open(LOG, encoding="utf-8"):
        e = json.loads(l)
        if e["id"] == eid:
            return e
    return {"error": f"unknown: {eid}"}
