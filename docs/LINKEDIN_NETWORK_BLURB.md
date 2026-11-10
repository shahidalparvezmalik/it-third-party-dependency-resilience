Across a career of more than 20 years in IT infrastructure, operations and service delivery, I have seen how difficult it can be to maintain one reliable view of what a service depends on. Service records, supplier information and technical diagrams each tell part of the story; the links between them need regular attention.

My new portfolio project explores that issue with a small Python proof of concept. It takes fictional service-to-provider records, groups services by provider and flags shared relationships or entries that still need confirmation. In the sample, Northstar Cloud supports four listed services and Acme Identity appears against three.

The tool produces a CSV review report and a JSON map. Its rules are deterministic and visible. The flags do not measure supplier risk, reveal relationships missing from the input or prove that a service can recover. They simply give service owners and technical teams a structured starting point for checking declared dependencies.

The repository includes the runnable CLI, synthetic sample data, tests and data dictionary. I would be interested to hear how other organizations maintain these records as services, architectures and suppliers change, and who is accountable for confirming them.

#IrishTech #IrishITTech #Ireland #Germany #Netherlands #Finland #Poland #ThirdPartyRisk #TechnologyResilience #OperationalResilience