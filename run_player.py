#run active player model
import sys
import time
import numpy as np
import Data
import low_model as model
import learners
import parameters


def run_player(n):
    
    #timing
    starttime=time.clock()

    #kids' data
    data=Data.Data()
    data.read(astext=False)
    n_kids=parameters.n_kids

    #parameters
    truncate=int(n)
    nr=parameters.n_r_random
    n_long_kids=sum([data.get_kid_nactions(kid)>=truncate \
                             for kid in data.get_kids()])

    #initialize variables    
    ps=np.zeros((n_long_kids,3))
    model_actions=[]
    random_actions=[]
    kid_actions=[]

    #iterate kids
    k=0
    for kind,kid in enumerate(data.get_kids()[:n_kids]):
        if data.get_kid_nactions(kid)<truncate:
            continue
        
        #get kid's action sequence
        kidseq=data.data[kid][:truncate]
        
        #initialize player
        active_player=learners.ActivePlayer()

        #compute success probability
        kid_action=kidseq[-1].action
        kid_actions.append(kid_action)
        kid_p=active_player.success_probability(kid_action, kidseq[:-1]) 

        model_action=active_player.choose_action(kidseq[:truncate-1])
        model_actions.append(model_action)
        model_p=active_player.success_probability(model_action, kidseq[:-1])

        random_p=0
        random_actions.append([])
        for r in range(nr):
            random_model=learners.RandomLearner()
            random_action=random_model.choose_action(kidseq[:truncate-1])
            random_actions[k].append(random_action)
            random_p+=active_player.success_probability(random_action, kidseq[:-1])

        random_p/=nr
        
        ps[k,0]=model_p
        ps[k,1]=random_p
        ps[k,2]=kid_p

        k+=1


    #save stuff
    filename=parameters.output_directory+'player-'+str(truncate)+'_tru-'\
            +str(nr)+'_rreal.txt'
    np.savetxt(filename, ps, fmt='%.5f')

    with open(parameters.output_directory+'player-modelactions-'+str(truncate)+'_tru-'+\
        str(nr)+'_nr.txt','w') as f:
        for action in model_actions:
            f.write(str(action)+'\n')

    with open(parameters.output_directory+'player-randomactions-'+str(truncate)+'_tru-'+\
        str(nr)+'_nr.txt','w') as f:
        for action in random_actions:
            f.write(str(action)+'\n')

    with open(parameters.output_directory+'player-kidactions-'+str(truncate)+'_tru-'+\
        str(nr)+'_nr.txt','w') as f:
        for action in kid_actions:
            f.write(str(action)+'\n')

    print 'time elapsed for run {0}: {1:.0f} s'.format(filename, time.clock()-starttime)




if __name__ == '__main__':
    if len(sys.argv)>1:
        n=int(sys.argv[1])
    else:
        n=1  
    run_player(n)


