# IT Third-Party Dependency Mapping: Shared providers are easy to miss

A critical service can depend on several suppliers, but the same technology provider may sit underneath multiple services. When those relationships live in separate spreadsheets, the shared dependency can be easy to overlook.

I built a small Python proof of concept to make those relationships visible in a consistent format. It reads a fictional service-to-provider register, groups services by provider, and flags shared providers and dependency entries that have not been confirmed.

## What the example shows

The sample contains five fictional services. Northstar Cloud appears against four of them; Acme Identity appears against three. The tool marks services linked to those shared providers for review. Two service records also have unconfirmed dependency status, which produces a separate verification flag.

These are review prompts, not risk scores. A provider appearing against several services does not, by itself, tell us the business impact, whether alternatives exist, or whether the organization has an effective contingency. Those questions require service owners and technical teams to check the relationships and supporting evidence.

## A map is only as good as its inputs

This demo uses deterministic rules and a small CSV file. It does not discover hidden dependencies, validate provider claims, assess fourth parties, inspect contracts, or test resilience. The criticality field is included as context but is not used by the rules. The output cannot establish compliance or prove that any service can withstand a supplier outage.

For an actual review, the map would need accountable owners, confirmed supplier relationships, change control, evidence, and a defined review cycle. The sample deliberately stops before making a treatment recommendation.

## Why I built it

My previous project, IT Service Continuity & Recovery Readiness, flags gaps in recovery records for individual services. This #9 project looks across services to see whether they rely on the same technology providers. It also sits alongside my vendor performance project, while keeping the scope distinct: supplier performance is different from shared dependency visibility.

The Business Continuity Institute has highlighted the need to map technology dependencies and identify concentration and single points of failure. The Central Bank of Ireland describes ICT third-party risk management as one of DORA's areas for regulated financial entities. Those are useful reasons to examine the problem; this proof of concept is not a DORA assessment.

## Try the project

The repository includes a standard-library Python CLI, synthetic CSV input, unit tests, and documentation. Run `python -m unittest discover -v`, then run the CLI command in the README to produce a review CSV and provider-to-service JSON map.

Project: https://github.com/shahidalparvezmalik/it-third-party-dependency-resilience  
Professional portfolio: https://shahidalparvezmalik.com/

Shahid Al Parvez Malik is a Senior IT Infrastructure & Service Delivery Manager with 20+ years of professional IT experience across enterprise infrastructure, IT Operations, ITSM, service delivery, systems administration, networking, technical support, procurement and vendor management.

#IrishTech #IrishITTech #Ireland #ITOperations #OperationalResilience #ThirdPartyRisk
