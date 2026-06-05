def singularize(word):

    if word.endswith("ies"):
        return word[:-3] + "y"

    if word.endswith("s"):
        return word[:-1]

    return word


def repair(schema, errors):

    repair_logs = []

    if not errors:
        return schema, repair_logs

    existing_tables = [
        table["name"].lower()
        for table in schema["db"]["tables"]
    ]

    existing_roles = [
        role["name"].lower()
        for role in schema["auth"]["roles"]
    ]

    for error in errors:

        # Missing DB Table Repair

        if "Missing DB table for endpoint" in error:

            endpoint = error.split("/")[-1]

            table_name = singularize(
                endpoint
            ).capitalize()

            if table_name.lower() in existing_tables:
                continue

            schema["db"]["tables"].append(
                {
                    "name": table_name,
                    "fields": [
                        {
                            "name": "id",
                            "type": "UUID"
                        }
                    ]
                }
            )

            repair_logs.append(
                f"Created missing table: {table_name}"
            )

            existing_tables.append(
                table_name.lower()
            )

        # Missing Admin Role Repair


        elif error == "Admin role missing":

            if "admin" not in existing_roles:

                schema["auth"]["roles"].append(
                    {
                        "name": "Admin",
                        "permissions": [
                            "all"
                        ]
                    }
                )

                repair_logs.append(
                    "Created missing Admin role"
                )

                existing_roles.append(
                    "admin"
                )

    return schema, repair_logs