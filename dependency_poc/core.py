"""Deterministic dependency aggregation and review flags."""
from collections import defaultdict

def analyze(rows):
    providers=defaultdict(set)
    for row in rows:
        for provider in filter(None,(x.strip() for x in row["providers"].split(";"))):
            providers[provider].add(row["service_id"])
    shared={k:v for k,v in providers.items() if len(v)>=2}
    result=[]
    for row in rows:
        names=sorted(x.strip() for x in row["providers"].split(";") if x.strip())
        flags=[]
        if row["verification"].strip().lower()!="confirmed": flags.append("VERIFY_DEPENDENCIES")
        overlap=sorted(n for n in names if n in shared)
        if overlap: flags.append("SHARED_PROVIDER_REVIEW")
        result.append({"service_id":row["service_id"],"service_name":row["service_name"],"provider_count":len(names),"shared_providers":";".join(overlap),"review_flags":";".join(flags) or "NONE"})
    graph={k:sorted(v) for k,v in sorted(providers.items())}
    return result,graph
