class operations:

 def calc_inv(mat):

  det = operations.calc_det(mat)
  adj = operations.calc_adj(mat)
  for i in range(3):
   for j in range(3):
    adj[i][j] /= det
  return adj
 
 def calc_det(mat):
  sum = 0
  for i in range(3):
   sum += pow(-1,i)*mat[0][i]*(mat[1][i-2 if i>1 else i+1]*mat[2][i-1 if i>0 else i+2]-mat[2][i-2 if i>1 else i+1]*mat[1][i-1 if i>0 else i+2])
  return sum

 def calc_adj(mat):

  adj_mat  = []
  for i in range(3):
   minor = []
   for j in range(3):
    minor_ele = pow(-1,i+j)*(mat[i-2 if i>1 else i+1][j-2 if j>1 else j+1] * mat[i-1 if i>0 else i+2][j-1 if j>0 else j+2] - mat[i-1 if i>0 else i+2][j-2 if j>1 else j+1] * mat[i-2 if i>1 else i+1][j-1 if j>0 else j+2])
    minor.append(minor_ele)                                            
   adj_mat.append(minor)
  return adj_mat
 
 def calc_prod(mat_a,mat_b):

  new_mat=[]
  for i in range(3):
   mat = []
   for j in range(3):
    ele = mat_a[j][i]*mat_b[i][j]
    mat.append(ele)
   new_mat.append(mat)
  return new_mat

 def calc_sub(mat_a,mat_b):
  diff_mat = []
  for i in range(3):
    for j in range(3):
      diff_mat[i][j] = mat_a[i][j]-mat_b[i][j]
  return diff_mat

 def calc_add(mat_a,mat_b):
  sum_mat = []
  for i in range(3):
    for j in range(3):
      sum_mat[i][j] = mat_a[i][j]+mat_b[i][j]
  return sum_mat