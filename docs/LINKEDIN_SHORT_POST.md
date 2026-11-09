A supplier can appear in a contract register while the services that depend on it are recorded somewhere else. That gap is easy to miss until someone asks a harder question: how many important services rely on the same technology provider?

After more than 20 years in IT infrastructure, operations and service delivery, I’ve seen how useful it is to make those relationships easier to discuss. For my latest portfolio project, I built a small Python proof of concept that maps fictional services to their declared technology providers. It groups services by provider and flags shared providers and unconfirmed dependency records for people to review.

👉 Read the full article and share your perspective:


The example uses deterministic rules and synthetic data. In the sample, Northstar Cloud appears across four services and Acme Identity across three. The code produces a CSV review report and a JSON provider map. Those flags are prompts, not risk scores or evidence that a real service is resilient—or not. The project does not discover hidden dependencies, assess suppliers, test recovery or make compliance claims.

I’ve kept the scope narrow on purpose: the point is to make the relationship and the rule visible, then leave validation and decisions with accountable service and technical owners. A provider count alone can’t tell us business impact, alternatives, recovery capability or whether a record is still current.

#IrishTech #IrishITTech #Ireland #Germany #Netherlands #Finland #Poland