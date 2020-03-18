

# -----------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------#
# ================================ 0302 号总结中的绘图======================================#
# -----------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------#

plotting.plotting_mix_ssmm_train(moea_list, sklearn_list, soea_list, op_targets, target, color = True, type = 2, if_show_label = True, save_folder = 'mix')

# ==============================linear-single-obj

#---------------------------plot
plotting.plotting_mix_ssmm_train(moea_list = [], sklearn_list = [4, 6], soea_list = [[1, 1], [1,3], [1,4],[1,5], [1,6], [1,7], [1,8], [1,9], [1,10]], op_targets=[], target=[0,4])
plotting.plotting_mix_ssmm_test(moea_list = [], sklearn_list = [4, 6], soea_list = [[1, 1], [1,2], [1,3], [1,4],[1,5], [1,6], [1,7], [1,8], [1,9], [1,10]], op_targets=[], target=[0,4])
#----------------------------table
make_tables.ssmm_table_train(moea_list = [], sklearn_list= [4,6], soea_list = [[1, 1], [1,3], [1,4],[1,5], [1,6], [1,7], [1,8], [1,9], [1,10]], op_targets = [], target=0)
make_tables.ssmm_table_test(moea_list = [], sklearn_list= [4,6], soea_list = [[1, 1], [1,3], [1,4],[1,5], [1,6], [1,7], [1,8], [1,9], [1,10]], op_targets = [], target=0)



# ================================mlp3-single

#-------------------------------plot
plotting.plotting_mix_ssmm_train(moea_list = [], sklearn_list = [4, 6], soea_list = [[5, 1], [5,3], [5,4],[5,5], [5,6], [5,7], [5,8], [5,9], [5,10]], op_targets=[], target=[0,4])
plotting.plotting_mix_ssmm_test(moea_list = [], sklearn_list = [4, 6], soea_list = [[5, 1], [5,3], [5,4],[5,5], [5,6], [5,7], [5,8], [5,9], [5,10]], op_targets=[], target=[0,4])

#------------------------------table
make_tables.ssmm_table_train(moea_list = [], sklearn_list= [4,6], soea_list =  [[5, 1], [5,3], [5,4],[5,5], [5,6], [5,7], [5,8], [5,9], [5,10]], op_targets = [], target=0)
make_tables.ssmm_table_test(moea_list = [], sklearn_list= [4,6], soea_list =  [[5, 1], [5,3], [5,4],[5,5], [5,6], [5,7], [5,8], [5,9], [5,10]], op_targets = [], target=0)


#==============================linear-multi-obj
#--------------------------plot
plotting.plotting_mix_ssmm_train(moea_list = [[1, 3], [1, 12], [1, 14]], sklearn_list = [4, 6], soea_list = [], op_targets=[[0, 3, 4]], target=[0,4])
plotting.plotting_mix_ssmm_test(moea_list = [[1, 3], [1, 12], [1, 14]], sklearn_list = [4, 6], soea_list = [], op_targets=[[0, 3, 4]], target=[0,4])

#--------------------------table
# 1
make_tables.ssmm_table_train(moea_list = [[1, 1], [1, 9], [1, 10], [1, 11]], sklearn_list= [4, 6], soea_list =  [], op_targets = [[0, 1], [0,2], [0,1,2], [0,4], [0,2,4],[0,3], [0,1,3], [0, 3, 4]], target=0)
make_tables.ssmm_table_test(moea_list = [[1, 1], [1, 9], [1, 10], [1, 11]], sklearn_list= [4, 6], soea_list =  [], op_targets = [[0, 1], [0,2], [0,1,2], [0,4], [0,2,4],[0,3], [0,1,3], [0, 3, 4]], target=0)
# 2
make_tables.ssmm_table_train(moea_list = [[1, 3]], sklearn_list= [4, 6], soea_list =  [], op_targets = [[0,2], [0,4], [0,2,4],[0,3],[0, 3, 4]], target=0)
make_tables.ssmm_table_test(moea_list = [[1, 3]], sklearn_list= [4, 6], soea_list =  [], op_targets = [[0,2], [0,4], [0,2,4],[0,3],[0, 3, 4]], target=0)

# 3
make_tables.ssmm_table_train(moea_list = [[1, 12], [1, 13], [1, 14]], sklearn_list= [4, 6], soea_list =  [], op_targets = [[0,4], [0,2,4],[0, 3, 4]], target=0)
make_tables.ssmm_table_test(moea_list = [[1, 12], [1, 13], [1, 14]], sklearn_list= [4, 6], soea_list =  [], op_targets = [[0,4], [0,2,4],[0, 3, 4]], target=0)
#==============================mlp3-multi-obj
#--------------------------plot
plotting.plotting_mix_ssmm_train(moea_list = [[5, 12], [5, 13], [5, 14]], sklearn_list = [4, 6], soea_list = [], op_targets=[[0,3,4]], target=[0,4])
plotting.plotting_mix_ssmm_test(moea_list = [[5, 12], [5, 13], [5, 14]], sklearn_list = [4, 6], soea_list = [], op_targets=[[0,3,4]], target=[0,4])

#--------------------------table
make_tables.ssmm_table_train(moea_list = [[5, 12], [5, 13], [5, 14]], sklearn_list= [4, 6], soea_list =  [], op_targets = [[0, 3, 4]], target=0)
make_tables.ssmm_table_test(moea_list = [[5, 12], [5, 13], [5, 14]], sklearn_list= [4, 6], soea_list =  [], op_targets = [[0, 3, 4]], target=0)
#==============================mlp5-multi-obj
#--------------------------plot
plotting.plotting_mix_ssmm_train(moea_list = [[6, 12], [6, 13], [6, 14]], sklearn_list = [4, 6], soea_list = [], op_targets=[[0,3,4]], target=[0,4])
plotting.plotting_mix_ssmm_test(moea_list = [[6, 12], [6, 13], [6, 14]], sklearn_list = [4, 6], soea_list = [], op_targets=[[0,3,4]], target=[0,4])

#--------------------------table
make_tables.ssmm_table_train(moea_list = [[6, 12], [6, 13], [6, 14]], sklearn_list= [4, 6], soea_list =  [], op_targets = [[0, 3, 4]], target=0)
make_tables.ssmm_table_test(moea_list = [[6, 12], [6, 13], [6, 14]], sklearn_list= [4, 6], soea_list =  [], op_targets = [[0, 3, 4]], target=0)

# -----------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------#
# ================================ 0314 号总结中的绘图======================================#
# -----------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------#


#============================单目标优化FPA的对应NONZ值--------------------------------------#
# ==============================linear-single-obj
#----------------------------table
make_tables.ssmm_table_train(moea_list = [], sklearn_list= [4,6], soea_list = [[1, 1], [1,3], [1,4],[1,5], [1,6], [1,7], [1,8], [1,9], [1,10]], op_targets = [], target=2)
make_tables.ssmm_table_test(moea_list = [], sklearn_list= [4,6], soea_list = [[1, 1], [1,3], [1,4],[1,5], [1,6], [1,7], [1,8], [1,9], [1,10]], op_targets = [], target=2)

# ================================mlp3-single

#------------------------------table
make_tables.ssmm_table_train(moea_list = [], sklearn_list= [4,6], soea_list =  [[5, 1], [5,3], [5,4],[5,5], [5,6], [5,7], [5,8], [5,9], [5,10]], op_targets = [], target=2)
make_tables.ssmm_table_test(moea_list = [], sklearn_list= [4,6], soea_list =  [[5, 1], [5,3], [5,4],[5,5], [5,6], [5,7], [5,8], [5,9], [5,10]], op_targets = [], target=2)


#============================nsga2结果和lasso的对比--------------------------------------#
plotting.plotting_universal_test(moea_list = [[1, 3, [0, 2]], [1, 3, [0, 4]], [1, 3, [0, 2, 4]]], sklearn_list = [4], soea_list = [], target=[0,4])
plotting.plotting_universal_train(moea_list = [[1, 3, [0, 2]], [1, 3, [0, 4]], [1, 3, [0, 2, 4]]], sklearn_list = [4], soea_list = [], target=[0,4])

plotting.plotting_universal_test(moea_list = [[1, 3, [0, 2]], [1, 3, [0, 4]], [1, 3, [0, 2, 4]]], sklearn_list = [4], soea_list = [], target=[0,2])
plotting.plotting_universal_train(moea_list = [[1, 3, [0, 2]], [1, 3, [0, 4]], [1, 3, [0, 2, 4]]], sklearn_list = [4], soea_list = [], target=[0,2])

#mlp和rf的对比
plotting.plotting_universal_test(moea_list = [[5, 12, [0, 3, 4]], [5, 13, [0, 3, 4]], [5, 14, [0, 3, 4]]], sklearn_list = [6], soea_list = [], target=[0,4])
plotting.plotting_universal_train(moea_list = [[5, 12, [0, 3, 4]], [5, 13, [0, 3, 4]], [5, 14, [0, 3, 4]]], sklearn_list = [6], soea_list = [], target=[0,4])



#============================ mlp3选取出来最优的值对应的mse的结果与rf的对比====================
train_ratio = 0.5,pratios=[1,0,0], random_size = 1

train_ratio = 0.5,pratios=[1,0,0], random_size = 0.5
train_ratio = 0.8,pratios=[8,4,1], random_size = 1
train_ratio = 0.8,pratios=[1,0,0], random_size = 1
 # save_file = 'balance_tvratio_test_' + para_name[target]
make_tables.make_balance_tvratio(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = 0, if_max = True, train_ratio = 0.5,pratios=[1,0,0], random_size = 1)
make_tables.make_balance_tvratio(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = 0, if_max = True, train_ratio = 0.5,pratios=[1,0,0], random_size = 0.5)
make_tables.make_balance_tvratio(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = 0, if_max = True, train_ratio = 0.8,pratios=[8,4,1], random_size = 1)
make_tables.make_balance_tvratio(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = 0, if_max = True, train_ratio = 0.8,pratios=[1,0,0], random_size = 1)

make_tables.make_balance_tvratio(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = 4, if_max = True, train_ratio = 0.5,pratios=[1,0,0], random_size = 1)
make_tables.make_balance_tvratio(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = 4, if_max = True, train_ratio = 0.5,pratios=[1,0,0], random_size = 0.5)
make_tables.make_balance_tvratio(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = 4, if_max = True, train_ratio = 0.8,pratios=[8,4,1], random_size = 1)
make_tables.make_balance_tvratio(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = 4, if_max = True, train_ratio = 0.8,pratios=[1,0,0], random_size = 1)

# 同时获取相应的fpa及mse值
make_tables.choose_model(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = [0, 4], if_max = True, train_ratio = 0.5,pratios=[1,0,0], random_size = 1)
make_tables.choose_model(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = [0, 4], if_max = True, train_ratio = 0.5,pratios=[1,0,0], random_size = 0.5)
make_tables.choose_model(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = [0, 4], if_max = True, train_ratio = 0.8,pratios=[8,4,1], random_size = 1)
make_tables.choose_model(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = [0, 4], if_max = True, train_ratio = 0.8,pratios=[1,0,0], random_size = 1)
make_tables.choose_model(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = [0, 4], if_max = True, train_ratio = 0.8,pratios=[1,1,1], random_size = 0.3)



make_tables.choose_model(moea_list = [[6, 13], [5, 14]], op_targets =[[0, 3, 4]], parameters = [0, 3, 4], target = [0, 4], if_max = True, train_ratio = 0.8,pratios=[1,1,1], random_size = 0.2)


make_tables.choose_model(moea_list = [[6, 13], [5, 14]], op_targets = [[0, 3, 4]], parameters = [0, 3, 4], tar)