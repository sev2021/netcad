# 13 LED dot martix emulation for digits 0-9
# EVEN MORE simpler version:

mat = ['#### ## ## ####', ' #  #  #  #  # ', '###  #####  ###',
'###  ####  ####', '# ## ####  #  #', '####  ###  ####', '####  #### ####',
'###  #  #  #  #', '#### ##### ####', '#### ####  ####']

sample_text = "1234567890"   # works only for string of digits 0-9!
for lin in range(5):
    print(*[mat[int(val)][lin*3:lin*3+3] for val in sample_text])

    
    
####################################
###### SECOND VERSION

# for lin in range(5):                  ## LED display has 5 lines
#     for val in "1234567890":          ## This is sample text, can ba any strnig of digits
#         print(mat[int(val)][lin*3:lin*3+3], end=' ')
#     print()



####################################
###### FIRST VERSION

# dd = {}
# dd["0"] = ['###','# #','# #','# #','###']
# dd["1"] = ['#','#','#','#','#']
# dd["2"] = ['###','  #','###','#  ','###']
# dd["3"] = ['###','  #','###','  #','###']
# dd["4"] = ['# #','# #','###','  #','  #']
# dd["5"] = ['###','#  ','###','  #','###']
# dd["6"] = ['###','#  ','###','# #','###']
# dd["7"] = ['###','  #','  #','  #','  #']
# dd["8"] = ['###','# #','###','# #','###']
# dd["9"] = ['###','# #','###','  #','###']


# for lin in range(5):
#     for val in "1234567890":
#         print(dd[val][lin], end=' ')
#     print()
