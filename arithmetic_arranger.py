import re

def arithmetic_arranger(problems): # change to accept conditional input
  print(problems)
  operator = listopertors(problems)
  newlist = []
  if len(problems) > 5:
    return "Error: Too many problems."
  else:
    for i in problems:
      if "/" in i or "*" in i:
        return "Error: Operator must be '+' or '-'."
      else:
        newword = re.split(r"[\+]*[\-]*[\s]",i)
        newlist.append(newword)

  for a in newlist:
    for j in a:
      if "" in a:
        a.remove("")
      if j.isdigit() == False:
        return "Error: Numbers must only contain digits."
      if len(j) > 4:
        print(j)
        return "Error: Numbers cannot be more than four digits."
  print(newlist)


  # for o in newlist:
  #   #for l in o:
  #   print('{:>5}'.format(*o))
  res1, res2 = map(list, zip(*newlist))
  print(res1)
  print(res2)

  # for j in res1:
  #   print('\t')

  # for k in res2:
  #   print('\t'+j)
  #for i in res1
  i = 0
  for i in range(0,len(operator)):
    print('{:>5}\n{:<1}{:>4}'.format(res1[i],operator[i],res2[i]).endswith(""))
    #print('-'*len())

  #for o,b in zip(res1,res2):
  # print('{:>5} {:>5} {:>5} {:>5} '.format(*res1))
  # print('{:<5} {:<5} {:<5} {:<5} '.format(*operator))
  # print('{:>5} {:>5} {:>5} {:>5} '.format(*res2))
  # print("\t32\t4\t4765")
  # print("\t2343\t43\t847")

def listopertors(list):
  signs = []
  for a in list:
    if "+" in a :
      val = "+"
      signs.append(val)
    elif "-" in a :
      val = "-"
      signs.append(val)
  return signs


# def maxoperand(list):
#   for a in list:
#     for k in a:
#       first = k
#       if k > first


# def dashnumber(string):