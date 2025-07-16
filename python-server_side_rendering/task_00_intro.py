def generate_invitations(template, attendees):
    """
    Generates personalized invitations for each attendee.
    Args:
        template (str): String
        attendees (list of dict): A list of dictionaries: 
        name, event_title, event_date, event_location.
    Prints
        if the template or the list of attendees is empty.
        if the template is not a string or if attendees is not a list.
        If any field is missing in the attendee dictionary,
        it will replace the missing data with "N/A".
    """
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return
    if not template:
        print("Template can't be empty.")
        return
    if not attendees:
        print("Attendees list can't be empty.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for i, attendee in enumerate(attendees, 1):
        content = template
        for key in placeholders:
            value = attendee.get(key, "N/A")
            content = content.replace(f"{{{key}}}", value)
        filename = f"output_{i}.txt"
        with open(filename, "w") as f:
            f.write(content)
