"""
experiment.py — Reproduzierbares Experiment-Logbuch für die RH-Forschung.

Jedes Experiment = {Hypothese, Methode, Parameter, Ergebnis, Schlussfolgerung, Zeit}.
Wird als JSON (maschinenlesbar) UND Markdown (lesbar) in kb/experiments/ gespeichert.
Ziel: nachvollziehbare Zusammenarbeit (z. B. mit einem Mathe-Professor).
"""
import os, json, time, hashlib

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "experiments")
os.makedirs(DIR, exist_ok=True)
LOG = os.path.join(DIR, "logbook.jsonl")

def log_experiment(hypothesis, method, params, result, conclusion="", tags=None):
    """Speichert ein Experiment reproduzierbar. params/result als JSON-fähige Dicts."""
    ts = time.strftime("%Y-%m-%dT%H:%M:%S")
    payload = {"hypothesis": hypothesis, "method": method, "params": params,
               "result": result, "conclusion": conclusion, "tags": tags or [],
               "time": ts}
    eid = "exp-" + hashlib.sha1(json.dumps(payload, sort_keys=True, default=str).encode()).hexdigest()[:10]
    payload["id"] = eid
    # JSONL anhängen
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False, default=str) + "\n")
    # Markdown-Einzeldatei
    md = _to_md(payload)
    with open(os.path.join(DIR, eid + ".md"), "w", encoding="utf-8") as f:
        f.write(md)
    return {"id": eid, "saved": True, "markdown": os.path.join(DIR, eid + ".md")}

def _to_md(p):
    return (f"# Experiment {p['id']}\n\n"
            f"- **Zeit:** {p['time']}\n"
            f"- **Tags:** {', '.join(p['tags']) or '—'}\n\n"
            f"## Hypothese\n{p['hypothesis']}\n\n"
            f"## Methode\n{p['method']}\n\n"
            f"## Parameter\n```json\n{json.dumps(p['params'], ensure_ascii=False, indent=2, default=str)}\n```\n\n"
            f"## Ergebnis\n```json\n{json.dumps(p['result'], ensure_ascii=False, indent=2, default=str)}\n```\n\n"
            f"## Schlussfolgerung\n{p['conclusion'] or '(offen)'}\n\n"
            f"> Hinweis: Numerische Ergebnisse sind Evidenz, kein Beweis (siehe docs/35).\n")

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
        return {"error": "kein Logbuch"}
    for l in open(LOG, encoding="utf-8"):
        e = json.loads(l)
        if e["id"] == eid:
            return e
    return {"error": f"unbekannt: {eid}"}
