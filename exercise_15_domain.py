def get_domain(email):
    parts = email.strip().lower().split("@")
    return parts[1] if len(parts) == 2 else None

emails = ["Tejas@Gmail.com", " rahul@company.co.in", "priya@gmail.com", "amit@company.co.in"]

domains = [get_domain(e) for e in emails]
print(domains)
print(sorted(set(domains)))