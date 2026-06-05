def normalize(name):

    return (
        name.lower()
        .replace("/", "")
        .replace("_", "")
        .replace("-", "")
    )


def singularize(word):

    if word.endswith("ies"):
        return word[:-3] + "y"

    if word.endswith("s"):
        return word[:-1]

    return word


def validate(schema):

    errors = []

    # ------------------------
    # Basic checks
    # ------------------------

    if "pages" not in schema["ui"]:
        errors.append("UI pages missing")

    if "endpoints" not in schema["api"]:
        errors.append("API endpoints missing")

    if "tables" not in schema["db"]:
        errors.append("DB tables missing")

    if errors:
        return errors

    # ------------------------
    # DB table names
    # ------------------------

    table_names = []

    for table in schema["db"]["tables"]:

        table_names.append(
            normalize(table["name"])
        )

    # ------------------------
    # Ignore special routes
    # ------------------------

    ignore_entities = [
        "auth",
        "dashboard",
        "reports",
        "analytics",
        "admin"
    ]

    # ------------------------
    # API ↔ DB validation
    # ------------------------

    for endpoint in schema["api"]["endpoints"]:

        path = endpoint["path"]

        parts = path.split("/")

        if len(parts) < 2:
            continue

        entity = normalize(parts[1])

        if entity in ignore_entities:
            continue

        singular = singularize(entity)

        if (
            entity not in table_names
            and singular not in table_names
        ):
            errors.append(
                f"Missing DB table for endpoint {path}"
            )

    # ------------------------
    # Auth validation
    # ------------------------

    role_names = []

    for role in schema["auth"]["roles"]:

        role_names.append(
            role["name"].lower()
        )

    has_admin = any(
        "admin" in role
        for role in role_names
    )

    if not has_admin:
        errors.append(
            "Admin role missing"
        )

    return errors