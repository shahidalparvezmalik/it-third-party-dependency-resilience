# IT Third-Party Dependency Mapping: Shared providers are easy to miss

After more than 20 years in IT infrastructure, operations and service delivery, I have learned that a supplier register and a service map answer different questions. A supplier register tells us who we buy from. A service map helps show what our important services depend on. When those views are kept apart, a technology provider supporting several services can be easy to miss.

That is the practical question behind my latest portfolio project: can a small, transparent tool make shared technology dependencies easier to see, without pretending to assess risk it cannot actually measure?

## When a provider appears in several places

Most organizations use a mix of cloud platforms, identity services, network providers, specialist applications and external support. A service owner may know the application supplier. Infrastructure teams may know the hosting provider. Procurement may hold the contract. Security may track an assessment. Each record can be useful, but it may not show the full chain between a business service and the technology providers that help deliver it.

That matters when teams are trying to understand concentration. If several important services depend on the same provider, a disruption to that provider could affect more than one service. The map does not prove that a disruption will happen, or that all dependent services will fail together. It does give people a concrete relationship to verify and discuss.

The same is true for a dependency that has not been confirmed. An empty field or an unverified entry is not proof that the service has no dependency. It is a signal that the record needs an owner and evidence before anyone relies on it.

## What I built

I built a compact Python proof of concept that reads a CSV register of services and their declared technology providers. It creates a provider-to-service map, counts how many distinct services refer to each provider, and flags two conditions for human review: providers linked to more than one service, and service records whose dependency confirmation is not marked as confirmed.

The project uses deterministic rules and fictional data. It does not use an AI model, connect to supplier systems, or discover dependencies automatically. The rule is visible in the code, so a reviewer can see why a relationship was flagged rather than receiving an unexplained risk score. In this example, “shared” means that a provider is recorded against at least two distinct services. That cutoff is a simple demonstration choice, not an industry benchmark or a claim that providers used by only one service are risk-free.

The sample register has five fictional services: Customer Portal, Online Payments, Workforce Collaboration, Finance Reporting and Endpoint Management. Across them, the fixture lists five providers. Northstar Cloud appears against four services, and Acme Identity appears against three. The other three providers each appear once. Two service rows are marked unconfirmed.

The program writes two outputs. A CSV review report gives one row per service, provider count, shared-provider names and review flags. A JSON map groups service identifiers under each provider. In the bundled example, five service rows have a shared-provider review flag, because every sample service uses either Northstar Cloud or Acme Identity. Two rows also carry the separate dependency-verification flag. Those are observed results from the fictional fixture, not findings about a real organization.

A reader can run the tests and the sample from the repository. The project uses Python's standard library, so the sample needs no external packages:

`python -m unittest discover -v`

`python -m dependency_poc.cli --input data/dependencies.csv --report reports/review.csv --map reports/map.json`

The test suite checks the shared-provider behavior and the case where a provider appears in only one service. The demonstration is intentionally small. Its purpose is to make the rule and the resulting review prompts inspectable, not to imitate a full third-party risk platform.

## A count is not a risk rating

Seeing a provider on four service records is a useful prompt. It is not, by itself, a measure of business risk. A count does not tell us the importance of each service, the provider's architecture, the likelihood or duration of an outage, contractual commitments, recovery arrangements, geographic exposure, substitutability, or whether the entries are accurate and current.

The project includes a criticality field in its sample data, but the current rules do not use it. That is deliberate. Adding a field to a CSV does not make the logic a business-impact analysis. I do not want a demo to imply that a simple formula can turn incomplete records into a defensible risk decision.

Nor does this version map fourth parties or deeper technology chains. A service may depend on an application provider that in turn depends on a cloud, identity, network or data service. The fixture records direct provider assertions only. It cannot infer those downstream relationships, test whether two apparently separate suppliers share infrastructure, or establish that an alternate provider is genuinely independent.

The project also does not review contracts, service-level agreements, provider assurance reports, backup evidence or recovery tests. It does not check live availability, model failure scenarios, set tolerances, recommend mitigations, certify compliance or trigger actions. Its output is not audit evidence or proof of resilience. Every relationship and flag needs review by someone accountable for the service and supported by suitable evidence.

## How I would use a map in a real review

I would start with the service owner and ask what the service does, who depends on it, and what would happen if it became unavailable. Then I would trace the technology relationships with the teams who own the applications, infrastructure, identity, networks and supplier records. The map is useful only if those people can confirm which relationships are current and which are assumptions.

For each shared provider, the follow-up should be a conversation rather than an automatic score. Which services depend on it? Are the relationships direct, or are there subcontractors and platform dependencies behind them? Are two providers genuinely independent, or do they share a common cloud, network, identity service or data centre? Which services have workable alternatives, and what evidence supports that conclusion?

A map also needs an owner and a review rhythm. Service changes, new applications, contract renewals, migrations and significant provider changes can make yesterday's dependency record stale. If nobody owns the map, it will gradually become a picture of how the organization used to work.

There is also a practical data problem: provider names are not always consistent. One team may use a product name, another the legal supplier name, and a third an internal abbreviation. Before counting relationships, an organization needs a stable way to identify providers and services. Otherwise, one supplier may appear as two names and the map may understate concentration. Conversely, broad labels such as “cloud” can merge unrelated providers and overstate it. The sample avoids that ambiguity by using simple, consistent fictional names; a real inventory would need defined identifiers and a process for maintaining them.

I would want the person reviewing the result to record the source of each relationship, who confirmed it, when it was checked, and what remains uncertain. That makes it easier to distinguish a verified dependency from a supplier name copied into a spreadsheet years ago. It also gives service owners a route to correct the record rather than treating the tool's output as a verdict. A review status should have a clear meaning, too: “confirmed” might refer to a service-owner check, technical validation, contract evidence, or a combination. Without that definition, a green status can mean different things to different teams.

Only after that groundwork would I connect the dependency view with business impact, recovery objectives, incident history, service performance, contractual evidence and scenario testing. Those inputs can support a more meaningful discussion about resilience, but each has its own definitions and quality limits. A dependency count cannot replace that work.

## How this fits with my other projects

This is project #9 in my GitHub portfolio. My IT Service Continuity & Recovery Readiness project looks at completeness indicators within individual service records, such as ownership, dependency confirmation and exercise dates. This project looks across service records to show where provider names are shared. The two views can inform different questions, but neither proves that a service can be recovered.

My IT Procurement & Vendor Performance Management project focuses on lifecycle visibility, supplier scorecards and renewal review. Supplier performance and service dependency mapping are related areas, but they are not the same analysis. A supplier can meet contractual measures while still supporting several services. A dependency map can show that a provider is shared without telling us whether its performance is good or poor.

That separation matters in practice. Combining every supplier, continuity, service-management and technical concern into one score can create the appearance of precision without making the assumptions any clearer. I prefer to keep the questions visible, explain the rules, and let accountable people decide what additional evidence or action is needed.

## Why the topic is getting attention

The Business Continuity Institute's resource on managing critical third-party technology dependencies discusses mapping technology relationships, hidden supplier risks, concentration and single points of failure. The Central Bank of Ireland's DORA information describes ICT third-party risk management among the areas covered for financial entities within the regulation's scope.

These sources explain why organizations are paying attention to technology providers and resilience. They do not validate this proof of concept, and the project is not a DORA assessment or compliance tool. Regulatory obligations depend on the entity, the applicable requirements and the evidence maintained by the organization. A small synthetic-data example cannot make that determination.

## What the project can and cannot offer

The repository offers a runnable example, sample CSV, tests, a data dictionary and a suggested human review sequence. It demonstrates one narrow task: group declared technology providers across fictional services and identify shared or unconfirmed relationships using simple, inspectable rules.

It cannot tell a reader whether their supplier records are complete, whether a provider is critical, whether a service will meet a recovery objective, or whether a mitigation is sufficient. It cannot see the organization's infrastructure or contact its suppliers. The sample contains no real company, service or vendor information. Please do not put confidential production data into the demonstration.

That boundary is useful to me. Tools can help organize a review, but the person accountable for a service still needs to decide whether the record is correct and what it means. Clear limits make it less likely that a tidy chart will be mistaken for assurance. If teams choose to adapt the example, they should document any changed thresholds and agree who can approve them; changing a number without explaining why does not make a review more meaningful.

## The project

I have published the proof of concept on GitHub. The repository contains the Python command-line demo, fictional input data, tests, a data dictionary, operating guidance and the LinkedIn companion materials:

https://github.com/shahidalparvezmalik/it-third-party-dependency-resilience

After more than two decades working across IT infrastructure, IT Operations, ITSM and service delivery, I remain interested in practical ways to make service relationships and operational assumptions easier to discuss. I would be interested to hear how other IT Operations and Service Delivery leaders connect supplier dependencies with service impact, resilience evidence and operational KPI reporting. What has helped your teams keep those records current?

## About the author

Shahid Al Parvez Malik is a Senior IT Infrastructure & Service Delivery Manager specializing in enterprise IT operations, ITSM, infrastructure, procurement and technology management.

Professional portfolio: https://shahidalparvezmalik.com/

#IrishTech #IrishITTech #Ireland #Germany #Netherlands #Finland #Poland