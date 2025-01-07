

def format_name(f_name,l_name):
  '''Takes name and convert it into caps'''
  f_name=f_name.title()
  l_name=l_name.title()
  return f'{f_name} {l_name}'
 



print(format_name(input('Enter first name : ').lower(),input('Enter last name : ').lower()))
