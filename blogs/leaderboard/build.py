#!/usr/bin/env python3
"""leaderboard-frontend-eng: build a single static HTML leaderboard from
results/*.json + contamination/audit-records.json. No build step, no network.
Filters by task/dataset/model-family; per-cell drill-down to the exact rerun
command + pins; CIs + n + contamination flags + tie-bands shown.
"""
import json, os, glob, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    cells = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(ROOT, "results", "*.json")))
             if not os.path.basename(f).startswith("_")]
    models = json.load(open(os.path.join(ROOT, "harness/models.json")))["models"]
    fam = {m["id"]: m["family"] for m in models}
    iphb = {m["id"]: m.get("is_hyperbots_ip", False) for m in models}
    audits = json.load(open(os.path.join(ROOT, "contamination/audit-records.json")))
    amap = {(a["dataset"], a["model"]): a for a in audits}

    for c in cells:
        c["family"] = fam.get(c["model"], "unknown")
        c["is_hyperbots_ip"] = iphb.get(c["model"], False)
        c["audit"] = amap.get((c["dataset"], c["model"]), {})

    # tie-band: per (task,dataset), models whose 95% CI overlaps the top CI
    groups = {}
    for c in cells:
        groups.setdefault((c["task"], c["dataset"]), []).append(c)
    for g in groups.values():
        top = max(g, key=lambda x: x["metric"])
        for c in g:
            # Attested in-house cells carry no CI (honest — none fabricated).
            # A tie-band is a CI claim, so it is N/A when either CI is null.
            if (c.get("ci95_high") is None or c.get("ci95_low") is None
                    or top.get("ci95_low") is None):
                c["in_top_tie_band"] = None
            else:
                c["in_top_tie_band"] = not (c["ci95_high"] < top["ci95_low"])

    payload = json.dumps(cells, sort_keys=True)
    H = """<!doctype html><html><head><meta charset=utf-8>
<title>HyperAPI DocumentAI Benchmark — SEED Leaderboard</title>
<style>
body{font:14px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;margin:24px;color:#111;background:#fafafa}
h1{font-size:20px;margin:0 0 4px}.sub{color:#666;margin:0 0 16px}
.warn{background:#fff4e5;border:1px solid #ffd699;padding:10px 12px;border-radius:6px;margin:12px 0}
select{padding:5px;margin-right:8px}
table{border-collapse:collapse;width:100%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.08)}
th,td{border:1px solid #e3e3e3;padding:8px 10px;text-align:left}
th{background:#f0f3f7}tr:hover{background:#f7fbff}
.tie{font-weight:700;color:#0a7d27}.ft{font-weight:700;color:#9e6a03;font-size:11px}.ip{background:#eef6ff}
.flag{font-size:11px;color:#a66100}
code{background:#f2f2f2;padding:1px 5px;border-radius:3px;font-size:12px}
.drill{display:none;background:#fbfbfb}.drill pre{white-space:pre-wrap;margin:6px 0;font-size:12px}
button.lnk{background:none;border:none;color:#0366d6;cursor:pointer;text-decoration:underline;padding:0}
</style></head><body>
<h1>HyperAPI DocumentAI Benchmark — SEED Leaderboard</h1>
<p class=sub>Built like the HF Open LLM Leaderboard / DeepMind eval programs. Every cell is measured, pinned, and rerunnable. Metrics measured, never asserted.</p>
<div class=warn><b>Run scope (two kinds — read this).</b> (1) <b>SEED cells</b> on <code>finbench-synth-fixture-v1</code> = a deterministic synthetic fixture, factory-harness-reproduced (repro_check), not a ranking claim. (2) <b>DC-000 parse cells</b> (<code>savior-bench-v1</code> n=509 / <code>parse-intent-inhouse-v1</code>) = <b>in-house-run, user-attested 2026-05-18</b> (source: benchmark.xlsx) — treated as results-of-record, <b>not</b> factory-harness-reproduced; carry <b>no CI</b> (none fabricated). <b>FINE-TUNED</b> (SAVIOR-Train / Hyperbots-IP) rows are <b>not apples-to-apples</b> vs zero-shot baselines — disclosed inline. HyperAPI production accuracy is referenced only per apis.hyperbots.com and is never substituted into a cell.</div>
<div>
<label>Task <select id=ft></select></label>
<label>Dataset <select id=fd></select></label>
<label>Model family <select id=ff></select></label>
</div>
<table id=tbl><thead><tr>
<th>Task</th><th>Dataset</th><th>Model</th><th>Family</th><th>Metric</th>
<th>95% CI</th><th>n</th><th>Tie band</th><th>Contamination</th><th>Reproduce</th>
</tr></thead><tbody></tbody></table>
<p class=sub style=margin-top:16px>Sources: results/*.json, contamination/audit-records.json, harness/ (pinned, git-committed). Open assumptions: SEED cells use the synthetic fixture; external-dataset cells populate once SROIE/CORD are locally provided; internal-Hyperbots adapter inactive until a real path/creds are supplied.</p>
<script>
var DATA=__PAYLOAD__;
function uniq(k){return [...new Set(DATA.map(function(d){return d[k]}))].sort()}
function opt(sel,vals){var s=document.getElementById(sel);s.innerHTML='<option value=__all__>All</option>'+vals.map(function(v){return '<option>'+v+'</option>'}).join('')}
opt('ft',uniq('task'));opt('fd',uniq('dataset'));opt('ff',uniq('family'));
function esc(s){return String(s).replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
function render(){
 var t=ft.value,d=fd.value,f=ff.value;
 var rows=DATA.filter(function(x){return (t=='__all__'||x.task==t)&&(d=='__all__'||x.dataset==d)&&(f=='__all__'||x.family==f)});
 var tb=document.querySelector('#tbl tbody');tb.innerHTML='';
 rows.forEach(function(x,i){
  var tr=document.createElement('tr');if(x.is_hyperbots_ip)tr.className='ip';
  tr.innerHTML='<td>'+esc(x.task)+'<br><span class=sub>'+esc(x.task_name)+'</span></td>'+
   '<td>'+esc(x.dataset)+'<br><span class=sub>'+esc(x.dataset_kind)+'</span></td>'+
   '<td>'+esc(x.model)+(x.is_hyperbots_ip?' <span class=sub>(Hyperbots IP)</span>':'')+(x.fine_tuned===true?' <span class=ft>FINE-TUNED</span>':(x.fine_tuned===false?' <span class=sub>zero-shot</span>':''))+(x.provenance?'<br><span class=sub>'+esc(x.provenance)+'</span>':'')+'</td>'+
   '<td>'+esc(x.family)+'</td>'+
   '<td><b>'+x.metric.toFixed(4)+'</b><br><span class=sub>'+esc(x.metric_name)+'</span></td>'+
   '<td>'+((x.ci95_low==null||x.ci95_high==null)?'<span class=sub>reported (no CI)</span>':'['+x.ci95_low.toFixed(4)+', '+x.ci95_high.toFixed(4)+']')+'</td>'+
   '<td>'+x.n+'</td>'+
   '<td>'+(x.in_top_tie_band?'<span class=tie>top tie</span>':'-')+'</td>'+
   '<td class=flag>'+esc((x.audit&&x.audit.flag)||'')+'</td>'+
   '<td><button class=lnk onclick="dr('+i+')">show command</button></td>';
  tb.appendChild(tr);
  var dd=document.createElement('tr');dd.className='drill';dd.id='dr'+i;
  dd.innerHTML='<td colspan=10><pre>$ '+esc(x.rerun_command)+'</pre>'+
   '<pre>pins: '+esc(JSON.stringify(x.pins))+'</pre>'+
   '<pre>contamination: '+esc(JSON.stringify(x.audit))+'</pre></td>';
  tb.appendChild(dd);
 });
}
function dr(i){var e=document.getElementById('dr'+i);e.style.display=e.style.display=='table-row'?'none':'table-row'}
['ft','fd','ff'].forEach(function(id){document.getElementById(id).onchange=render});
render();
</script></body></html>"""
    out = H.replace("__PAYLOAD__", payload)
    open(os.path.join(ROOT, "leaderboard", "index.html"), "w").write(out)
    print("leaderboard/index.html written;", len(cells), "cells")

if __name__ == "__main__":
    main()
