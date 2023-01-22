from matrix_operations import operations as op 

mat_a = [[1,0,0],[0,1,0],[0,0,1]]
mat_b = [[1,0,0],[0,2,0],[0,0,3]]

mat_invB = op.calc_inv(mat_b)
mat_invA = op.calc_inv(mat_a)

MatAns_1 = op.calc_prod(mat_a,mat_invB)
MatAns_2 = op.calc_prod(mat_invA,mat_invB)

print(MatAns_1)
print(MatAns_2)





  


