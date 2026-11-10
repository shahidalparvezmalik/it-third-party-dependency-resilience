# When the same technology provider supports several services

In IT operations, an outage rarely respects the way we divide work between teams. A service owner may track the application, infrastructure colleagues know the hosting arrangement, and procurement holds the contract. Each view can be accurate and still miss an important connection: the same technology provider may sit underneath several services.

I have spent more than two decades working across IT infrastructure, operations and service delivery. One lesson from that work is that useful decisions depend on knowing what a service actually relies on, not just who owns the contract or the application. That question led me to build a small proof of concept for my portfolio: a clear way to surface shared provider relationships without pretending a simple map can measure resilience.

## The gap between service records and supplier records

Most organizations have plenty of information about suppliers and services. The difficulty is that the information may live in different places and use different names. A business service register may identify an application. A procurement record may identify the contracted supplier. An infrastructure diagram may show a hosting platform. A security review may name a subprocessor. Unless those relationships are connected, looking at one service at a time can hide dependencies that span the portfolio.

That matters when someone asks what could be affected by a provider disruption. If several services rely on the same provider, the potential impact may cross team or business-unit boundaries. The existence of a shared provider does not prove that an incident will occur, or that all affected services would fail together. It does give service owners and technical teams a specific relationship to check.

Unconfirmed information deserves the same care. A missing or unverified dependency does not mean there is no dependency. It means the record is not yet strong enough to support a confident conclusion. That distinction is easy to lose when a spreadsheet looks complete simply because every row has something in it.

## A small, inspectable example

The project reads a CSV containing fictional services and their declared technology providers. It groups service identifiers under each provider, counts distinct services, then flags two cases for human review: a provider associated with more than one service and a service record whose dependency status is not confirmed.

The rules are deterministic and visible in the code. The demo does not use an AI model, connect to live supplier systems or discover hidden relationships. “Shared” has a narrow meaning here: a provider appears in the records for at least two distinct services. That threshold is only a demonstration rule, not a standard for measuring risk.

The sample contains five fictional services: Customer Portal, Online Payments, Workforce Collaboration, Finance Reporting and Endpoint Management. It lists five providers. Northstar Cloud appears against four services; Acme Identity appears against three. Each of the other providers appears once, and two service records are marked unconfirmed.

Running the example creates a CSV review report with one row per service, the number of declared providers, shared-provider names and review flags. A JSON file groups the services by provider. In this fixture, all five service rows receive a shared-provider flag because each refers to Northstar Cloud or Acme Identity. Two rows also receive the separate verification flag. These are results from fictional input, not observations about any real organization.

The repository includes a standard-library Python command-line tool, tests, the example data, a data dictionary and operating notes. To run it:

`python -m unittest discover -v`

`python -m dependency_poc.cli --input data/dependencies.csv --report reports/review.csv --map reports/map.json`

The example is deliberately modest. Someone reviewing the code can trace how the input becomes a flag and can change the rule if they have a justified reason. The output is meant to start a review, not to grade a supplier or service.

I chose CSV for the example because most teams can inspect it without a specialist platform. It also makes the input and result easy to compare during a review. The JSON map provides a second view that other tools could consume, but neither format solves the hard part: deciding who owns each relationship and how it stays current. A larger implementation would need access controls, change history, data lineage and a defined source of truth. None of those controls are part of this proof of concept.

The tests focus on the rule, not on whether a supplier is safe. They check that a provider used by multiple services is surfaced and that a provider recorded once is not mistakenly treated as shared. The demo output is repeatable, which makes it easier to review a change to the code or sample. That kind of transparency is more useful here than a sophisticated interface that hides its assumptions.

## What the map cannot tell us

A provider count is not a risk score. Seeing one supplier linked to four services does not tell us how critical those services are, how likely an outage might be, how long it could last, or what alternatives are available. It does not show whether the services share the same infrastructure, whether contracts include useful commitments, or whether recovery arrangements have been exercised.

The sample has a criticality field, but the current rules do not use it. I have kept that distinction explicit: having a field called “criticality” does not mean the program has assessed business impact. The current logic does not weight services, calculate exposure or recommend a treatment.

It also records direct provider assertions only. It cannot follow a chain from an application supplier to a hosting platform, identity service, network or fourth party. Two suppliers that look independent in a register may still rely on the same downstream technology. This version cannot find that out. It cannot validate supplier declarations, read contracts, inspect assurance reports, test recovery, check live availability or determine compliance with DORA or any other regulation.

That boundary is important. A tidy map can look more authoritative than the information behind it. Every relationship needs an owner, a source and a confirmation date. A flag should lead to a conversation with the people who understand the service, not to an automatic conclusion about the provider.

## Turning a list into something a team can maintain

If I were using this idea in an operational review, I would start with service owners and ask them to confirm the services, their purpose and the technology relationships they know about. I would then bring in the application, infrastructure, identity, network and procurement teams to validate the entries and identify where evidence is missing.

Provider names need consistent identifiers. One team may use a product name, another the legal supplier name, and a third an internal abbreviation. If these refer to the same provider, the map could understate concentration; if a broad label combines unrelated suppliers, it could overstate it. The demo uses consistent fictional names, but a working inventory needs an agreed naming convention and a way to resolve duplicates.

The status “confirmed” also needs a shared definition. Does it mean that the service owner has acknowledged the entry? That a technical owner has validated it? That contract or architecture evidence supports it? Those checks are not interchangeable. A team should record what was checked, by whom and when, then keep the relationship current as services, suppliers and designs change.

The review should look beyond whether a provider appears more than once. Which services depend on it? Are the dependencies direct? Do supposedly separate providers share a platform or network? Could a service move to an alternative, and has that alternative been tested? What recovery evidence supports the answer? These are questions for the organization, not calculations this proof of concept can perform.

I would also separate confirming a record from deciding what to do about it. A team may verify that a provider supports a service and still need a separate impact assessment to decide whether the relationship needs deeper analysis. If the dependency is uncertain, the next step may be to find the right technical owner or consult an architecture record. If the relationship is confirmed, the team can then decide whether to test an alternative, review contract evidence or update its continuity planning. Those actions depend on the organization's service context and risk process; the demo does not prescribe them.

That distinction matters in a meeting. A flag should not be read aloud as “high risk” when the tool has only counted service references. The reviewer should be able to say what is known, what remains unverified, and who will follow up. If a concern needs escalation, it should move through the organization's normal governance rather than acquiring authority from a color or number in a report.

Changes to applications, contracts, migrations and service architecture can all make a dependency map stale. An owner and review cycle are therefore part of the work, not administrative extras. If the records have no steward, they will eventually describe how the organization used to operate.

Only after the relationships are checked would I connect them with service impact, recovery objectives, incident history, contractual evidence and scenario testing. Those sources can support a more grounded resilience discussion. A count of supplier names cannot substitute for them.

## How this project fits my portfolio

This is project #9 in my GitHub portfolio. My IT Service Continuity & Recovery Readiness project looks at completeness indicators within individual service records, including ownership, dependency confirmation and exercise dates. This one looks across records to show where provider names are shared. They address different questions; neither proves that a service can be recovered.

My IT Procurement & Vendor Performance Management project focuses on lifecycle visibility, supplier scorecards and renewal review. A supplier can meet its performance measures and still support several services. Likewise, a dependency map can show that a provider is shared without telling us whether that supplier performs well. Keeping those questions separate makes the limits of each view clearer.

The Business Continuity Institute's resource on managing critical third-party technology dependencies discusses mapping relationships, concentration and single points of failure. The Central Bank of Ireland's DORA information describes ICT third-party risk management for financial entities within the regulation's scope. Those references help explain why the topic matters. They do not validate this demo, and the project is not a compliance assessment.

## What is in the repository

The repository contains the Python CLI, fictional CSV input, unit tests, data dictionary, operating guidance and companion LinkedIn copy. The code uses only Python's standard library. The sample data has no real suppliers or services, and it should not be replaced with confidential production information.

The project has a deliberately narrow purpose: make declared provider relationships easier to inspect and give reviewers a consistent starting point. It cannot tell an organization that its inventory is complete, that a supplier is critical, or that a recovery plan will work. Those conclusions require accurate information, accountable owners and evidence beyond this tool.

I have worked through more than 20 years of infrastructure and service-delivery questions, and I still find the basics matter most: clear ownership, reliable records and a shared understanding of what depends on what. I built this proof of concept to make one part of that conversation easier to start. How do you keep technology dependency records current across service, IT and procurement teams, and what evidence do you use before treating a relationship as confirmed?

## The project

GitHub repository: https://github.com/shahidalparvezmalik/it-third-party-dependency-resilience

## About the author

Shahid Al Parvez Malik is a Senior IT Infrastructure & Service Delivery Manager specializing in enterprise IT operations, ITSM, infrastructure, procurement and technology management.

Professional portfolio: https://shahidalparvezmalik.com/

#IrishTech #IrishITTech #Ireland #Germany #Netherlands #Finland #Poland