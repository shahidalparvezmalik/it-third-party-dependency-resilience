I’ve published a new portfolio proof of concept on IT third-party technology dependency mapping. The idea came from a practical question: when teams look at important services one by one, how easily can they spot that several of them rely on the same provider?

The small Python demo uses fictional service and provider records. It groups services by provider and flags shared-provider relationships and unconfirmed dependencies for human review. In the sample data, Northstar Cloud appears against four services, while Acme Identity appears against three. The program creates a CSV review report and a JSON map, using deterministic rules that can be inspected and tested.

These results are not supplier risk scores. A provider appearing across several services does not, by itself, show the business impact of an outage, the chance of one, the availability of alternatives or whether recovery arrangements would work. The demo does not discover hidden dependencies, validate provider declarations, test resilience or establish regulatory compliance. The sample data is fictional, and the tool is not intended for confidential production records.

The project sits alongside my work in service continuity and vendor management, while keeping a distinct focus: showing declared provider relationships across services. In a real environment, service owners and technical teams would need to confirm the records, document the evidence and keep the map current as services and suppliers change.

I’d be interested to hear how other IT Operations and Service Delivery leaders maintain visibility of shared technology dependencies, and how they connect that view with service impact, recovery evidence and operational KPIs.

#IrishTech #IrishITTech #Ireland #Germany #Netherlands #Finland #Poland