{
 'name':'Library Management',
 'description':'Manage library book catalogue and lending',
 'author':'Daniel Reis',
 'depends':['base'],
 'application':True,
 'data':[
  'views/library_menu.xml',
  'security/library_security.xml', 
  'security/ir.model.access.csv',
 ],
}