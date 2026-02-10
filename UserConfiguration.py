def add_setting(settings, new_pair):
    key, value = new_pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings.update({ key : value })
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, pair):
  key, value = pair
  key = key.lower()
  value = value.lower()

  if key in settings:
        settings.update({ key : value })
        return f"Setting '{key}' updated to '{value}' successfully!"
  else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
  key = key.lower()

  if key in settings.keys():
    settings.pop(key)
    return f"Setting '{key}' deleted successfully!"
  else:
    return "Setting not found!"

def view_settings(settings):
  if len(settings.keys()) == 0:
    return "No settings available."
  else:
    output = 'Current User Settings:\n'

    for i in settings.keys():
      output += f"{i.capitalize()}: {settings[i]}\n"

    return output

test_settings = {
    'por' : 'ddd',
    'ggtrtg' : 'hbrtr'
}