from tabulate import tabulate

students =[
     ['Trisha','python', 90],
     ['Alice','JavaScript', 98],
     ['Bob','SQL', 91],
     ['Charlie','Java', 70],
     ['David','C++', 80]
]

print(tabulate
      (students, headers=['Name', 'Subject', 'Marks'], 
               tablefmt='rounded_grid')
      )