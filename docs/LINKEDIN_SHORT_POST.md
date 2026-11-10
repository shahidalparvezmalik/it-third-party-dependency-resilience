A service register can name the team responsible for an application and still leave one important question unanswered: which other services depend on the same technology provider?

In my 20+ years across infrastructure and IT service delivery, I’ve seen how supplier and service information can end up in separate records. For project #9 in my GitHub portfolio, I built a small Python example that brings one part of that picture together. It maps fictional services to declared providers and flags shared providers or unconfirmed relationships for people to check.

👉 Read the full article and share your perspective:


The sample shows Northstar Cloud linked to four services and Acme Identity to three. The program exports a CSV review report and a JSON provider map. It uses simple, visible rules; the flags are not risk ratings, and the demo cannot discover hidden dependencies or test recovery.

I kept the scope narrow because a count alone cannot explain service impact, alternatives or whether a record is current. Those questions still need input from service owners and technical teams. The repository includes the runnable CLI, sample data, tests and a data dictionary so readers can inspect how the demo works. It uses synthetic data and is not a compliance assessment.

#IrishTech #IrishITTech #Ireland #Germany #Netherlands #Finland #Poland