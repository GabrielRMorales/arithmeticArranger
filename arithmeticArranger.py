def arithmetic_arranger(problems):
  data={
    "topNumbers": [],
    "bottomNumbers": [],
    "signs": [], 
    "answers": [],
    "spaces": []
  }
  #set to do this for each element in list
  for i in problems:
    firstProblem = i.split()
    sign=firstProblem[1]
    if sign=="+":
    # calculate if one number has a bigger tens value
      if int(firstProblem[0])>int(firstProblem[2]):
        topNumber=firstProblem[0]
        bottomNumber=firstProblem[2]
        
      elif int(firstProblem[0])<int(firstProblem[2]):
        topNumber=firstProblem[2]
        bottomNumber=firstProblem[0]
      answer=int(firstProblem[0])+int(firstProblem[2])
    else:
      #assume sign in minus
      topNumber=firstProblem[0]
      bottomNumber=firstProblem[2]
      answer=int(topNumber)-int(bottomNumber)

    if (int(topNumber)>999):
      space=5
    elif (int(topNumber)>99):
      space=4
    elif (int(topNumber)>9):
      space=3
    
    #go back and convert all the data to strings with the specific number of spaces for each
    #then print that 
    data["spaces"].append("-"*space)
    data["signs"].append(" "*(space-1)+str(sign))
    data["topNumbers"].append(str(topNumber)+" "*space)
    data["bottomNumbers"].append(str(bottomNumber))
    data["answers"].append(str(answer))
    #for x, y in enumerate(problems):
    #  print(f"{x}\n")
    #  print(f"{y}\n")
    #push the info into an object then iterate through and print that stuff
  
  print(" ".join(data["topNumbers"]))
  print(" ".join(data["signs"]))
  print(" ".join(data["bottomNumbers"]))
  print(" ".join(data["spaces"]))
  print("    ".join(data["answers"]))
  #for i in range(0, len(data)):
  #  print(f"{data['topNumbers'][i]}", end=" ")
  #  print(f"{data['sign'][i]} {data['bottomNumbers'][i]}", end=" ")
  #  print("-----",)
  #  print(f"{data['answer'][i]}\n",)
  return problems
#def get_place_val(num):

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
#len()
#int()



