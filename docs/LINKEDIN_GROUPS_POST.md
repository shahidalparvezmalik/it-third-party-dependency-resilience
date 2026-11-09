One provider can sit behind several services, yet the information needed to see that relationship may be split across service records, procurement files and technical inventories. A map can help make that overlap visible—but only if people understand what it does and does not tell them.

I’ve built a small Python proof of concept for my portfolio that groups fictional IT services by their declared providers. It flags providers referenced by more than one service and records where a dependency is not confirmed. The demo is deterministic, uses synthetic data, and produces a CSV review report alongside a JSON map.

👉 Read the full article and share your perspective:


In the fixture, Northstar Cloud appears against four services and Acme Identity against three. That is a useful prompt to ask questions: are the relationships current? Are they direct or are there other providers behind them? Do the affected services have genuinely independent alternatives? The program cannot answer those questions. It does not discover suppliers, assess actual risk, test recovery or establish compliance.

After 20+ years in IT infrastructure, operations and service delivery, I’m interested in tools that help teams have a clearer conversation—not tools that replace service-owner judgement with a number. For a real inventory, each relationship needs an owner, a source, a confirmation date and a way to keep it current as services change.

How does your team keep service owners, IT, procurement and suppliers aligned when dependencies change? And what evidence do you rely on before treating a relationship as confirmed?

#IrishTech #IrishITTech #Ireland #Germany #Netherlands #Finland #Poland