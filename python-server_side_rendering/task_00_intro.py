def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list of attendees.
    
    Args:
        template (str): The template string with placeholders.
        attendees (list): A list of dictionaries containing attendee information.
    """
    # Check if template is a string
    if not isinstance(template, str):
        print(f"Error: Template must be a string, not {type(template).__name__}")
        return
    
    # Check if attendees is a list
    if not isinstance(attendees, list):
        print(f"Error: Attendees must be a list, not {type(attendees).__name__}")
        return
    
    # Check if template is empty
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Check if all items in attendees are dictionaries
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: All attendees must be dictionaries")
        return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        # Create a copy of the template
        personalized_invitation = template
        
        # Replace placeholders with attendee information
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder, "N/A")
            if value is None:  # Handle None values
                value = "N/A"
            personalized_invitation = personalized_invitation.replace(f"{{{placeholder}}}", str(value))
        
        # Write to output file
        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w') as file:
            file.write(personalized_invitation)
