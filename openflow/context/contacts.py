import platform
import subprocess

def run_applescript_capture(script):
    """
    Runs the given AppleScript using osascript, captures the output and error, and returns them.
    """
    # print("Running this AppleScript:\n", script)
    # print(
    #     "---\nFeel free to directly run AppleScript to accomplish the user's task. This gives you more granular control than the `computer` module, but it is slower."
    # )
    args = ["osascript", "-e", script]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    stdout, stderr = result.stdout, result.stderr
    return stdout, stderr

def get_email_address(contact_name):
    """
    Returns the email address of a contact by name.
    """
    if platform.system() != 'Darwin':
        return "This method is only supported on MacOS"
    
    script = f'''
    tell application "Contacts"
        set thePerson to first person whose name is "{contact_name}"
        set theEmail to value of first email of thePerson
        return theEmail
    end tell
    '''
    stout, stderr = run_applescript_capture(script)
    # If the person is not found, we will try to find similar contacts
    if "Can’t get person" in stderr:
        return None
    else:
        return stout.replace('\n', '')

def get_all_names():
    """
    Returns a list of full names of contacts that contain the first name provided.
    """
    if platform.system() != 'Darwin':
        return "This method is only supported on MacOS"
    
    script = f'''
    tell application "Contacts"
        set allPeople to every person
        set namesList to {{}}
        repeat with aPerson in allPeople
            set end of namesList to name of aPerson
        end repeat
        return namesList
    end tell
    '''
    names, _ = run_applescript_capture(script)
    if names:
        return names
    return None

def get_full_names_from_first_name(first_name):
    """
    Returns a list of full names of contacts that contain the first name provided.
    """
    if platform.system() != 'Darwin':
        return "This method is only supported on MacOS"
    
    script = f'''
    tell application "Contacts"
        set matchingPeople to every person whose name contains "{first_name}"
        set namesList to {{}}
        repeat with aPerson in matchingPeople
            set end of namesList to name of aPerson
        end repeat
        return namesList
    end tell
    '''
    names, _ = run_applescript_capture(script)
    if names:
        return names
    return None
