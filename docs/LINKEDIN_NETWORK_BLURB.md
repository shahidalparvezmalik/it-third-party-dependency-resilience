My career has spanned more than two decades in IT infrastructure, operations and service delivery. One recurring challenge is getting a clear view of what each service depends on when the information sits across team registers, technical records and supplier files.

I’ve added a new proof of concept to my GitHub portfolio that explores that problem in a narrow, practical way. The Python demo takes fictional service-to-provider records, groups services by provider and flags shared relationships or entries that still need confirmation. In the sample, Northstar Cloud appears against four services and Acme Identity against three.

The output is a CSV review report and a JSON map. The logic is deterministic and visible, so a reviewer can see what triggered each flag. It is not a supplier risk score or a resilience assessment. The example cannot find undeclared dependencies, check supplier evidence, assess business impact or prove that recovery will work. Its data is synthetic, and it is not intended for confidential operational records.

I see it as a starting point for a better conversation between service owners, technical teams and procurement: which relationships are verified, who owns them, and how do we keep them current as services change? I’d be interested to hear what approaches have worked in your organization.

#IrishTech #IrishITTech #Ireland #Germany #Netherlands #Finland #Poland