# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:36:18 2022

@author: Junior
"""

import numpy as np
import math
import matplotlib.pyplot as plt




def V(r):           #repulsion at short distances, attraction at long (cohesion)
    return 3.5*(r+5)*math.log((r+5)/20)*np.exp(-((r+5)/25)**2)

    
def phi(r):         #positive everywhere and goes to 0 as r gets large - alignement 
    return (2.1*(0.2*r -0.4)**4)/np.exp(0.2*r -0.4)


def omega(x):     #gets larger the closer you get to 0 (closer sheep gets to wall)
    return 8*np.exp(-0.1*x)

def F2(x):     #calculates distance from sheep to centre of circle (500,500)
    centre = np.array([563,563])    
    return np.subtract(centre,x)
def F1(x):
    centre = np.array([563,563])
    return np.subtract(x,centre)

def acceleration(x,v):     
    n = len(x)
    accelerationlist = []
    for i in range(n):
        Fone = F1(x[i])
        Ftwo = F2(x[i])
        a= np.zeros(2)
        for j in range(n):
            if i == j:
                pass
            else:
                r = np.linalg.norm(x[i]-x[j]) #the distance between i^th and j^th sheep
                
                a = np.add(a,(1/n)*phi(r)*np.add(v[i],v[j])) #alignement
                a = np.add(a,(1/n)*V(r)*(np.subtract(x[j],x[i])/r)) #repulsion/attraction
                a = np.add(a,omega(563-np.linalg.norm(Ftwo))*Ftwo/np.linalg.norm(Ftwo)) #inner radius force
                a = np.add(a,omega(np.linalg.norm(Fone)-250)*Fone/np.linalg.norm(Fone)) #outer radius force
        accelerationlist.append(a)
    return accelerationlist



def velocitycap(v): #takes all the velocities and ensures |v|<= 1
    n = len(v)
    for i in range(n):
        magnitude = np.linalg.norm(v[i])
        if magnitude <= 1:
            pass
        else:
            v[i] = (v[i] / magnitude)*1
    return v #returns the velocities which now all have magnitude <= 1

###### TESTING SECTION ######
def avg_pos(x):    # the average position of the flock    
    return np.sum(x, axis=0)/len(x)

def avg_vel(x):    # the average velocity of the flock
    return np.sum(x, axis=0)
def nearestneighbour(a,x,i):
    x = np.delete(x,i, axis = 0)    #gets rid of current vector in list to avoid getting 0 distance
    n = len(x)
    distances = []       # list filled with ther distances from a to ith vector
    for i in range(n):
        distances.append(np.linalg.norm(np.subtract(x[i],a)))
    distances = np.sort(distances)
    # print(distances)
    
    return [distances[0],distances[1]]   
def expanse(x):
    n = len(x)
    avg = avg_pos(x)
    ans = 0
    for i in range(n):
        ans += np.linalg.norm(np.subtract(avg,x[i]))
    
    return (ans / n)   #/ ((xdim**2 +ydim**2)**0.5)/2
def NND(x):    # the nearest neighbour distance
    n = len(x)
    n1 = 0
    n2 = 0
    for i in range(n):
        val = nearestneighbour(x[i],x,i)
        n1 += val[0]
        n2 += val[1]
    n1 = n1 / n
    n2 = n2 / n
    # print("n1 =",n1)
    # print("n2 =",n2)
    return (n2-n1) #/ (xdim**2 +ydim**2)**0.5
def polarisation(x):
    n = len(x)
    avg = avg_vel(x)
    ans = []
    
    for i in range(n):
        cosangle = np.dot(avg,x[i])/np.linalg.norm(x[i])/np.linalg.norm(avg)
        angle = np.arccos(cosangle)
        ans.append(angle)
        
    ans = np.sum(ans, axis=0)/n
    return  np.degrees(ans) #/ 90
    

##### TESTING SECTION FINISHED ######

def iterations(x,v,t): #time iterations     
    timelist = []
    NNDlist =[]
    expanselist = []
    polarisationlist =[]    
    for i in range(t):
        x = np.add(x,velocitycap(v))
        v = np.add(v,acceleration(x,v))
        
        # if i%10 == 0:    # comment out if just want to show sheep
        #     timelist.append(i)
        #     NNDlist.append(NND(x))
        #     expanselist.append(expanse(x))
        #     polarisationlist.append(polarisation(velocitycap(v)))
        
            
    return x , velocitycap(v), timelist, NNDlist, expanselist, polarisationlist

# def iterations(x,v,t): #time iterations - no time dependence    
#     timelist = []
#     NNDlist =[]
#     expanselist = []
#     polarisationlist =[]    
#     t=0
#     while True:
#         x = np.add(x,velocitycap(v))
#         v = np.add(v,acceleration(x,v))
        
#         if t%10 == 0:    # comment out if just want to show sheep
#             timelist.append(t)
#             expanselist.append(expanse(x))
#             # polarisationlist.append(polarisation(velocitycap(v)))
#         if t ==3000:
#             print('h(3000)=',NND(x))
#         if expanse(x)<9.8:
#             print('time until single flock',t)
#             return x , velocitycap(v), timelist, NNDlist, expanselist, polarisationlist
#         t=t+1   

###100 sheep
x=np.array([[1030.9368657171713, 441.9054144573725], [353.4933835738737, 351.99968172719423], [345.97960825564405, 964.1299883346616], [639.0157831256897, 275.4230863151368], [273.09719402457563, 422.3055077005484], [136.37812225440416, 440.0379636139264], [784.1206078378057, 967.9096810249459], [516.2063912392973, 964.5599283804981], [819.2177435561623, 974.1597110973091], [495.8273162148402, 879.3671896777535], [397.5105107667375, 816.951527058801], [681.0980304651474, 62.68023745862422], [31.33514411083695, 676.8737483254042], [214.80715512156468, 127.58716468830471], [298.9409165977534, 557.5348837314828], [134.79462404927511, 776.0613514968891], [1075.3818576613276, 385.61291772010213], [406.9652108892535, 313.8041556217457], [932.2583228603489, 884.6848371889635], [930.7985742831306, 863.6776240159174], [850.5872969962395, 623.2345689017046], [670.7845467883844, 982.3020518197218], [609.782333256591, 281.6691470557451], [469.94866136829864, 306.6253797568025], [576.6954526776201, 883.3002879708233], [93.63330843704938, 828.0021426085932], [111.89467141887985, 886.5602315268064], [826.2473376706771, 817.9754493681904], [874.9612018302796, 532.5476115436171], [617.7982453862154, 146.151741065971], [761.048510148514, 355.5038733754635], [172.17838082759113, 515.0721417097163], [1017.5871917943341, 281.34447259743524], [1106.9774434201913, 683.3298931519741], [144.22054515798834, 880.8324607870331], [410.10759261679345, 1078.7605961032264], [249.1810937409985, 346.4339449438974], [826.0913177175746, 160.855887373744], [198.91818457137936, 405.3486142455771], [683.8105468430264, 1097.4222360894128], [247.40808265593552, 906.0710158239139], [210.37496261588484, 830.3264551770958], [713.758652663472, 1100.0573165947367], [937.4401439674821, 782.8241107959213], [1025.2685195235683, 278.837299979485], [492.07201181665323, 179.80514231662795], [312.0107958621817, 494.15252818402075], [19.428212355546407, 698.3616202861946], [833.6066197569946, 819.5942115053995], [678.7547674850313, 833.8441430126245], [989.0356725632394, 447.5849548438442], [798.2035220716962, 1053.5778836488403], [423.99765128246554, 91.53486922590662], [347.20812024484803, 231.2299216840076], [153.357062050897, 493.6524557330215], [946.9412957095958, 832.912496202679], [681.1097115063828, 1059.4379904227062], [461.7721975193242, 799.3217128485695], [867.9188462206153, 517.9962867738872], [754.4621361303311, 255.4940930689994], [234.9503766479615, 861.5731207190138], [748.9245491906188, 179.95946253926462], [216.69830323197112, 864.0110813716947], [1109.9253023885412, 636.534970272749], [1044.4322738572544, 813.5161222244701], [1019.0243309853535, 598.4861347895305], [707.7913344133772, 878.3748981719555], [24.934938410194945, 556.836524286582], [426.62586282443806, 332.06872342608847], [474.308825309516, 972.7192341713884], [98.05588085367737, 774.5783384561512], [137.36292542179086, 503.9895644734663], [202.05493010392536, 246.5783629933294], [166.00569996152183, 862.1892809907399], [465.8270131776414, 298.5349791456354], [940.6572631899951, 171.32499547465602], [1077.0087744758357, 473.971354559991], [881.5988330625373, 430.60250185339953], [552.5082518976085, 103.96340553259483], [1044.6541530679476, 326.3555760020249], [745.9086111702891, 1090.1652369395501], [279.75325322283373, 917.1376464018921], [1019.561271687019, 343.1584410291721], [674.4415475035261, 219.7689888735615], [60.45948301420344, 705.4834128240202], [185.74626736375046, 738.9001667185238], [197.0006939533252, 931.0307139793281], [522.7292472902268, 847.251915288795], [343.02778877116566, 826.1388323289575], [869.516661372943, 843.7075242630893], [398.6727592136943, 961.9035140100232], [574.3037578990305, 844.2161444498499], [210.12983603517296, 717.9158318540981], [641.8404550717329, 1035.3286258318801], [534.8652274502223, 135.7402781808383], [1088.919956305892, 371.1926806155111], [945.622145705613, 445.82086875044445], [253.3536442740346, 110.05457817095538], [300.5613715563385, 506.3239678962833], [871.4892745480975, 1011.3112159773298]])

v=np.array([[-0.329944222226459, -0.4222494325021249], [0.09809128937036016, 0.09783139068677171], [0.2755867662356054, -0.09540275572608703], [-0.36831326780930773, -0.06805081448442052], [0.02553408640062227, -0.3182123885557895], [0.4790598150400839, 0.44993980262871025], [-0.2908154696010202, 0.023252918823023938], [0.449710344329425, -0.3485145847289557], [-0.43690918651509725, 0.3212569124720821], [-0.32150367078205133, 0.235865696239294], [0.2429710847261103, -0.20700085824947212], [-0.2748580431479086, 0.23358008545423392], [0.2842573874164126, -0.10611661940678774], [-0.12415815756283499, -0.13786540476679954], [0.008204472459560352, 0.05864882460319765], [0.2917979599735928, 0.14973402198535402], [0.1498472284276252, 0.45029969168384243], [-0.07617596891045597, 0.28592760659466654], [-0.2508814069610099, 0.48046193488438527], [-0.11538569428158152, -0.48083860750149254], [-0.05589583194052805, -0.3061775399141974], [0.3236870370383481, -0.3385639061947787], [-0.2409169024664306, -0.29215892447193736], [0.051278088769503904, 0.38959928450560255], [-0.3042426674905666, -0.37080585195999116], [0.3680331252491925, -0.3772625664569268], [0.44977883207671554, 0.34276881640979184], [-0.14726188137211105, -0.12566837190075475], [-0.2255903311011216, -0.403931641664957], [-0.07068090204375066, -0.13051447406564265], [-0.3504060640984821, 0.17201004106687423], [0.3381281732731731, 0.48087534346395855], [0.2892497708532269, 0.025094994658722447], [0.4830566194618744, 0.00027227896272075114], [0.3769060616954737, -0.12697934317624981], [-0.12607733122144404, 0.45105882204826075], [0.028265107095782338, -0.26541694863991216], [-0.3518369152325843, 0.37010692122044664], [0.4695325385414526, 0.3045983956636974], [-0.2098959204560249, -0.4665941464110809], [-0.17098217524725867, 0.4280917304591263], [-0.2503975801519468, -0.3442780043786472], [0.3408830932100285, -0.3573202027854441], [-0.1004152156630036, 0.1812457283053328], [0.4225866471265395, -0.0480256143143607], [0.1490692238859671, 0.3065612390756971], [-0.453512410522503, 0.002503792145467032], [-0.17362060934673595, -0.17043371842124178], [0.025724341141369123, -0.04263108640031643], [-0.021393181835428154, 0.3979379987338858], [0.2180947081825435, -0.038710687999523596], [0.20662349816928605, -0.016057694083734142], [-0.047929624094151246, 0.08038206463016295], [-0.0952392998884194, 0.39398875416429324], [-0.2630186745426376, -0.46819426550586796], [-0.40499408176173346, -0.23342511153191192], [-0.4230006519397608, 0.30975366704950436], [0.0664278915320613, 0.46142449498450777], [0.12821122365482396, 0.12563121505528585], [-0.3927109391224032, 0.4384251325793974], [-0.31253325531421083, 0.35427531884108265], [0.38428625410661643, -0.27631265942357397], [0.48383841489823876, -0.4261872570486829], [0.34364320644149504, 0.35727633244952683], [-0.26210845752421885, 0.03128146905365392], [-0.48406280052235584, -0.3311900065257807], [0.2395289767279799, 0.20989038061898757], [-0.39966016229529777, -0.3099289337180815], [0.14811685089976323, 0.31082023010950155], [-0.473393615089048, 0.29837360565657955], [0.48324106970331093, 0.0023457893340854685], [-0.0971059843819152, 0.1388349599886799], [-0.3595034207906548, 0.12713392453436156], [-0.20803487531214582, 0.33909049028848004], [0.4384049007580598, -0.3045871458086252], [0.11077115156209727, -0.4531159505061607], [0.08654749824605967, -0.32412027518814424], [0.2827300776464071, 0.239580815956015], [-0.4831827008294083, 0.1775434132209418], [0.11201523126742652, -0.12978025111622393], [0.06616691222346005, 0.44446312336312], [0.46604636301589386, 0.46478705658540764], [0.17115728705535804, -0.21448771844630166], [-0.21127692297073064, 0.23196493562980292], [0.18281149698897603, 0.32772509407812933], [0.15673722521764832, -0.015015183300504109], [-0.2725311177342229, -0.25695548890413067], [-0.42719421184303796, -0.0013909548733770372], [0.09039220749767007, -0.16892217336292215], [-0.1359713827058444, -0.17371193327215118], [-0.24773634394377486, -0.1620735544690871], [0.28994092752847744, -0.3454407328189101], [0.21991271128992884, -0.02045480528439214], [-0.03534951227480987, -0.27269583563296906], [-0.3274048415756048, -0.29353344395163417], [-0.2533269208682094, -0.19159230961302642], [0.09949511872805927, -0.032945742316604076], [0.2959302764360825, 0.018143443520936664], [0.44960268072046783, -0.4225485662422175], [0.17731460830567347, 0.20750067830903496]])

t = 0 #NUMBER OF TIMESTEPS

result = iterations(x,v,t)
finalpositions = result[0]
finalvelocities = result[1]
timelist = result[2]
NNDlist = result[3]
expanselist = result[4]
polarisationlist = result[5]


n=len(x)
x=[]
y=[]
for i in range(n):
    x.append(finalpositions[i][0])
    y.append(finalpositions[i][1])


circle1 = plt.Circle((563, 563), 563, color='g',alpha=0.1)
circle2 = plt.Circle((563, 563), 250, color='white',alpha=1)
plt.figure(0)    
plt.gca().add_patch(circle1)
plt.gca().add_patch(circle2)
plt.scatter(x,y)
# plt.ylim(0,1200)
# plt.xlim(0,1200)
plt.gca().set_aspect('equal')
plt.show()

### STRENGTH OF FLOCKING ###

plt.figure(1)
plt.scatter(timelist,NNDlist, color = 'blue')
plt.title("Nearest Neighbour Distance")
plt.xlabel("Time-steps")
plt.ylabel("h(t) (d)")
plt.show()

plt.figure(2)
plt.scatter(timelist,expanselist ,color = 'red')
plt.title("Expanse")
plt.xlabel("Time-steps")
plt.ylabel("a(t) (d)")
plt.show()

plt.figure(3)
plt.scatter(timelist,polarisationlist , color = 'green')
plt.title("Polarisation")
plt.xlabel("Time-steps")
plt.ylabel("p(t) (degrees)")
plt.ylim(0,90)
plt.show()



print("polarisation",polarisation(finalvelocities))
print("expanse",expanse(finalpositions))
print("homogeneity",NND(finalpositions))

    