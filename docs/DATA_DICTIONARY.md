# Data dictionary

Input: `data/dependencies.csv`; all values are fictional.

- `service_id`: stable sample identifier for the service.
- `service_name`: fictional service label.
- `criticality`: supplied example label; not interpreted or validated.
- `providers`: semicolon-separated asserted technology providers.
- `verification`: relationship confirmation status; only the literal `confirmed` is treated as confirmed.

Report fields: `service_id`, `service_name`, `provider_count`, `shared_providers`, `review_flags`. The provider map JSON maps each provider name to sorted service IDs.
