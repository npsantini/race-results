import tkinter as tk
import csv

class Person:
  def __init__(self, rank, name, gender, age, chipTime, gunTime, pace):
    self.rank = rank
    self.name = name
    self.gender = gender
    self.age = age
    self.chipTime = chipTime
    self.gunTime = gunTime
    self.pace = pace

def sortByName(runnerObject, rWidget):
  #Sort by rank to keep the times in order
  sortByRank(runnerObject, rWidget)
  
  tableHeader = runnerObject[0]
  del runnerObject[0]
  
  runnerObject.sort(key=lambda x: x.name)
  rWidget.grid_remove()
  p.insert(0, tableHeader)
  displayResults(runnerObject)
  
def sortByAge(runnerObject, rWidget):
  #Sort by rank to keep the times in order
  sortByRank(runnerObject, rWidget)

  tableHeader = runnerObject[0]
  del runnerObject[0]
  
  runnerObject.sort(key=lambda x: x.age)
  rWidget.grid_remove()
  p.insert(0, tableHeader)
  displayResults(runnerObject)

def sortByRank(runnerObject, rWidget):
  tableHeader = runnerObject[0]
  del runnerObject[0]
  
  runnerObject.sort(key=lambda x: x.rank)
  rWidget.grid_remove()
  p.insert(0, tableHeader)
  displayResults(runnerObject)

#displayResults - Function to print the results in a text widget
def displayResults(runnerObject):

  #Initialize Column Headers
  text1 = tk.Text(root, height=45, width=55)
  text1.grid(column=0, row=1)
  text1.insert(tk.INSERT, '%-5s' % p[0].rank)
  text1.insert(tk.INSERT, " ")
  text1.insert(tk.INSERT, '%-30s' % p[0].name)
  text1.insert(tk.INSERT, " ")
  text1.insert(tk.INSERT, '%-3s' % "Sex")
  text1.insert(tk.INSERT, " ")
  text1.insert(tk.INSERT, '%6s' % p[0].age)
  text1.insert(tk.INSERT, " ")
  text1.insert(tk.INSERT, '%-7s' % "Time")
  text1.insert(tk.INSERT, "\n")
  text1.insert(tk.INSERT, "-" * 55)
  text1.insert(tk.INSERT, "\n")

  #Populate the results list
  j = 1
  while (j < i - 1):
      text1.insert(tk.INSERT, '%-5s' % p[j].rank)
      text1.insert(tk.INSERT, " ")
      text1.insert(tk.INSERT, '%-30s' % p[j].name)
      text1.insert(tk.INSERT, " ")
      text1.insert(tk.INSERT, '%-6s' % p[j].gender)
      text1.insert(tk.INSERT, " ")
      text1.insert(tk.INSERT, '%-3s' % p[j].age)
      text1.insert(tk.INSERT, " ")
      text1.insert(tk.INSERT, '%-7s' % p[j].chipTime)
      text1.insert(tk.INSERT, "\n")
      text1.insert(tk.INSERT, "-" * 55)
      text1.insert(tk.INSERT, "\n")
      j = j + 1

  text1.config(state="disabled")



#Initialize and populate the runner object
p = []
i = 0
with open('race-results.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        #Add 0 to single digit ages
        if (len(row[3]) < 2):
          row[3] = "0" + str(row[3])

        #Add 0's to ranks less than 100
        if (len(row[0]) < 2):
          row[0] = "00" + str(row[0])
        elif (len(row[0]) < 3):
          row[0] = "0" + str(row[0])
          
        p.append(Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        i = i + 1
#-----------------------------------------------

root = tk.Tk()
root.title("Race Results App")

resultsArea = tk.Frame(root)
resultsFrame = tk.Frame(resultsArea)

resultsArea.grid(column=0, row=0)
resultsFrame.grid(column=0, row=0, columnspan=3, rowspan=2)

btn1 = tk.Button(resultsArea, text="Sort By Name", width=20)
btn1.grid(column=0, row=0)

btn2 = tk.Button(resultsArea, text="Sort By Age", width=19)
btn2.grid(column=1, row=0)

btn3 = tk.Button(resultsArea, text="Sort By Rank", width=20)
btn3.grid(column=2, row=0)

#Display initial list
text1 = tk.Text(root, height=45, width=55)
text1.grid(column=0, row=1)

displayResults(p)
#------------------------------------------

#Button Commands
btn1['command'] = lambda arg1 = p, arg2 = text1 : sortByName(arg1, arg2)
btn2['command'] = lambda arg1 = p, arg2 = text1 : sortByAge(arg1, arg2)
btn3['command'] = lambda arg1 = p, arg2 = text1 : sortByRank(arg1, arg2)


root.mainloop()
