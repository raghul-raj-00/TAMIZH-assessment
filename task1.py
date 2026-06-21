def minruntime(bcap,binit,task,btrate):
    tottime=0.0
    battery=float(binit)
    for duration,drainrate in task:
        reqenergy=duration*drainrate
        if(reqenergy>bcap):
            return -1
        if(battery<reqenergy):
            if(btrate==0):
                return -1
            chargediff=reqenergy-battery
            idletime=chargediff/btrate
            tottime+=idletime
            battery+=chargediff
        tottime+=duration
        battery-=reqenergy
    return round(tottime,1)
#giving some testing inputs to check it is working            
bcap=100
binit=60
task=[[10,4],[5,8],[4,5]]
btrate=10
print(minruntime(bcap,binit,task,btrate))
