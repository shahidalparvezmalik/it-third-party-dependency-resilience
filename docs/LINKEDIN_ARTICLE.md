# IT Third-Party Technology Dependency & Resilience Mapping

In more than two decades working across IT infrastructure, operations and service delivery, I have seen service teams make careful plans around an incomplete picture. The application may be listed. The owner may be clear. The recovery procedure may be documented. Yet the provider that supports several services can still be hidden across separate supplier records, diagrams and spreadsheets.

That gap is the subject of my latest portfolio project, IT Third-Party Technology Dependency & Resilience Mapping. I built a small Python proof of concept to make declared service-to-provider relationships easier to inspect. Its purpose is deliberately modest: show where a provider appears across several services and identify records that still need confirmation, so people can decide what to review next.

## A service view and a supplier view answer different questions

A supplier register usually helps answer questions about the commercial relationship: who provides a product, which contract applies and when it renews. A service register answers different questions: what the service does, who owns it and who relies on it. Technical diagrams may show hosting, identity, network or data dependencies. These records all have value, but they are often maintained for different purposes by different teams.

When teams review each service on its own, they may not see that several services rely on the same technology provider. That overlap is worth checking because a disruption or change at the provider could have implications beyond one service. The relationship alone does not tell us how serious those implications would be. It does give service owners, infrastructure teams and procurement a concrete fact to validate together.

The quality of the record matters just as much. A provider relationship marked “unconfirmed” should not quietly be treated as either true or false. It is a prompt to find the right owner, check the source and record what has actually been verified. A completed spreadsheet can still contain uncertainty; a blank cell is not the only sign of missing information.

## What the proof of concept does

The program reads a CSV register of fictional services and their declared providers. It counts how many distinct services refer to each provider, creates a provider-to-service map and flags two conditions for human review: a provider associated with more than one service, and a service whose dependency status is not confirmed.

The rules are deterministic and visible in the Python code. No AI model is used. The tool does not connect to supplier systems, scan infrastructure or discover dependencies that are missing from the file. “Shared provider” has one narrow meaning in this example: the provider appears against at least two distinct services. That threshold is a demonstration choice, not a risk standard.

The sample register includes five fictional services: Customer Portal, Online Payments, Workforce Collaboration, Finance Reporting and Endpoint Management. It contains five fictional providers. Northstar Cloud is listed against four services, while Acme Identity appears against three. The remaining three providers appear once each, and two service records have an unconfirmed dependency status.

The tool writes two outputs. The CSV review report has one row per service, with the number of providers, shared-provider names and review flags. The JSON file groups service identifiers by provider. In this fixture, all five service records receive a shared-provider flag because each refers to Northstar Cloud or Acme Identity; two also receive a separate verification flag. Those counts describe the synthetic sample only. They are not findings about a live organization.

The repository includes the Python command-line interface, sample data, unit tests, a data dictionary and operating notes. It uses only the Python standard library. The commands to test and run it are:

`python -m unittest discover -v`

`python -m dependency_poc.cli --input data/dependencies.csv --report reports/review.csv --map reports/map.json`

The code is intentionally easy to inspect. A reviewer can trace a provider entry through to the resulting flag and see why it was included. The tests check the shared-provider rule and the case where a provider appears only once. They do not assess whether any supplier is safe or whether the output is complete.

## A count is a prompt, not a risk rating

Four service records linked to one provider may be a reason to ask further questions. The number does not tell us how critical those services are, whether they share an underlying platform, what an outage would mean, how long it might last or whether alternatives are available. It says nothing about the likelihood of a failure or the effectiveness of recovery arrangements.

The sample data includes a criticality field, but the program does not use it. A column with that name is not a business-impact analysis. The current rules do not weight services, calculate exposure or recommend treatments. They also do not establish whether service records are accurate, current or complete.

This version records direct provider assertions only. It cannot trace a relationship through an application provider to a cloud platform, identity service, network operator or fourth party. Two suppliers that appear independent in a register may rely on the same underlying technology; this tool cannot identify that shared infrastructure. It does not validate supplier declarations, examine contracts or assurance reports, test recovery, check live availability or assess compliance with DORA or another regulation.

Those limits matter because a clear-looking map can be mistaken for stronger evidence than it is. Each relationship needs an owner, a source and a confirmation date. A flag should guide a conversation with the people who understand the service. It should not be relabelled as “high risk” simply because the provider name appears more than once.

## How I would use the information in a real review

I would begin with the service owner, not with the score or flag. I would confirm what the service does, who depends on it and which technology relationships are known. Then I would ask the application, infrastructure, identity, network and procurement teams to validate the entries and point out where the source is uncertain.

Provider names need consistent identifiers. One team may record a product name, another the legal supplier name and a third an internal abbreviation. If those entries refer to one provider, inconsistent naming can hide concentration. At the other extreme, a broad label such as “cloud” could combine separate providers and overstate it. A working inventory needs a naming convention and a way to resolve duplicates; the simple sample avoids that problem by using consistent fictional names.

The status “confirmed” also needs a shared definition. It could mean the service owner has acknowledged the relationship, a technical owner has validated it, or supporting architecture or contract evidence has been checked. Those are different forms of confirmation. A useful record states what was checked, who checked it and when.

Once a relationship is validated, the next question is what it means for the service. Are two providers genuinely independent, or do they share a platform, network or identity service? Could the service move to an alternative, and has that alternative been tested? Which recovery evidence supports the plan? The proof of concept cannot answer these questions, but its map can help the right people see where to ask them.

I would also keep verification separate from treatment. Confirming that a provider supports a service does not automatically mean the relationship is unacceptable. A team may need an impact assessment, contract review, architecture analysis or recovery exercise before deciding what to do. If an entry is uncertain, the immediate task may simply be to locate a technical owner or source document. The organization’s governance and risk process should determine whether anything needs escalation.

Keeping the map current is part of that work. Applications change, contracts renew, services move and providers update their technology. A named owner and review cycle give teams a way to revisit the relationships rather than relying on an old snapshot. For each entry, I would want to know its source, last confirmation date and accountable owner, and to have a clear route for correcting it.

Only after those basics are in place would I connect the provider map to business impact, recovery objectives, incident history, contractual commitments and scenario testing. Those sources can support a broader resilience review. A count of provider names cannot replace them.

The review should also be proportionate to the service and the decision at hand. A shared provider may call for a basic ownership check in one case and a deeper architecture or recovery review in another. The tool cannot make that distinction because it does not interpret service impact. Service owners and the organization’s risk process have to decide what evidence is appropriate and how urgent the follow-up should be.

I would keep the follow-up traceable: record the question raised, the person responsible for answering it, the evidence considered and the date the record should be reviewed again. This is not extra scoring. It gives the next reviewer context and prevents a flagged row from circulating without an owner or a clear outcome. If the organization decides no further action is needed, that conclusion should still reflect the evidence and service context, rather than the absence of a warning from a small script.

## How this project relates to my other work

This is project #9 in my GitHub portfolio. IT Service Continuity & Recovery Readiness looks at completeness indicators inside an individual service record, including ownership, dependency confirmation and exercise dates. This project compares records across services to show where provider names are shared. They address related but different questions, and neither proves that recovery will work.

IT Procurement & Vendor Performance Management focuses on supplier lifecycle visibility, scorecards and renewal review. A supplier may meet its performance measures while supporting several services. A dependency map may show the shared relationship without indicating whether the supplier’s performance is good or poor. Separating those views makes it easier to see what each one can support and where more evidence is needed.

The Business Continuity Institute’s resource on [managing critical third-party technology dependencies](https://www.thebci.org/resource/managing-critical-third-party-technology-dependencies.html) discusses mapping relationships, concentration and single points of failure. The Central Bank of Ireland’s [DORA information](https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora) describes ICT third-party risk management among the areas relevant to financial entities within the regulation’s scope. These sources provide context for the topic; they do not validate this proof of concept. The project is not a DORA assessment or compliance tool.

## The project

The repository contains the command-line demo, fictional CSV input, unit tests, data dictionary and operating guidance. It is intended as a transparent example and a discussion starter, not a tool for processing confidential production records.

GitHub repository: https://github.com/shahidalparvezmalik/it-third-party-dependency-resilience

After more than 20 years in infrastructure and service delivery, I remain interested in the operational detail behind a service: who owns it, what it relies on and how confidently teams can answer those questions. This project makes one small part of that picture easier to examine. It gives teams a manageable starting point for verification, while leaving interpretation and decisions with accountable people and evidence. How does your organization keep technology dependency records current across service, IT and procurement teams?

## About the author

Shahid Al Parvez Malik is a Senior IT Infrastructure & Service Delivery Manager specializing in enterprise IT operations, ITSM, infrastructure, procurement and technology management.

Professional portfolio: https://shahidalparvezmalik.com/

#ThirdPartyRisk #TechnologyResilience #OperationalResilience #IrishTech #IrishITTech #Ireland #Germany #Netherlands #Finland #Poland