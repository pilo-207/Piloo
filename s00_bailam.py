"""
--- debai 
Viet python ham hi(name)
Tra ve cau chao 'Hi {name}'

--- input 
hi(name)

--- output
Hi {name}

--- ví dụ 1
hi('AI-BTX')

output
Hi AI-BTX

--- ví dụ 2
hi('HSU')

output
Hi HSU
"""

def hi(name):
  return f'Hi {name}'
  pass 
  #TODO

if __name__=='__main__':
  hi('AI-BTX')  # should see Hi AI-BTX
  hi('HSU')     # should see Hi HSU
