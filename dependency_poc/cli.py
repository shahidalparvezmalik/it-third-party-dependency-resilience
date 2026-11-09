"""CSV input to review CSV and provider-to-service JSON map."""
import argparse,csv,json
from pathlib import Path
from .core import analyze

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("--input",required=True);p.add_argument("--report",required=True);p.add_argument("--map",required=True)
 a=p.parse_args()
 with open(a.input,newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
 if not rows: raise SystemExit("input contains no service rows")
 report,graph=analyze(rows)
 for path in (a.report,a.map):Path(path).parent.mkdir(parents=True,exist_ok=True)
 with open(a.report,"w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=report[0].keys());w.writeheader();w.writerows(report)
 with open(a.map,"w",encoding="utf-8") as f:json.dump(graph,f,indent=2);f.write("\n")
 print(f"Services reviewed: {len(report)}")
 print(f"Providers mapped: {len(graph)}")
 print(f"Services flagged for review: {sum(r['review_flags']!='NONE' for r in report)}")
 print(f"Report: {a.report}");print(f"Map: {a.map}")
if __name__=="__main__":main()
