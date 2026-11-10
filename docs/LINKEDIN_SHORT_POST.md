A supplier register may show who provides a technology. A service catalogue may show which services matter. The connection between the two is often harder to see, especially when provider relationships are recorded differently across teams.

My work in IT infrastructure and service delivery spans more than 20 years. I built this project to explore a practical question from that experience: can a simple, transparent map help teams identify where a provider appears across several services, and where the underlying record still needs confirmation?

IT Third-Party Technology Dependency & Resilience Mapping is a small Python proof of concept using fictional data. It groups declared services by provider and flags shared-provider relationships and unconfirmed entries for human review. The sample shows Northstar Cloud linked to four services and Acme Identity to three. It creates a CSV review report and a JSON map.

👉 Read the full article and share your perspective:


The flags are not risk ratings. The program cannot discover undeclared dependencies, establish business impact or test recovery. Its value is narrower: make the stated relationships visible so service owners and technical teams can verify them and decide whether further work is needed.

The repository includes the CLI, sample input, tests and data dictionary. What helps your team keep provider dependencies accurate as services and suppliers change?

#ThirdPartyRisk #TechnologyResilience #OperationalResilience #IrishTech #IrishITTech #Ireland #Germany #Netherlands #Finland #Poland