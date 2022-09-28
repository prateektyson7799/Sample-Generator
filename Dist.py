###################################################################################################
# Author :  Nama Sai Krishna Prateek
# UTA ID : 1001880903
# Description : This program generates sample random numbers for the distributiions and calculates
#               Sample Mean and Sample Standard Deviation
# Citations : 1)https://www.youtube.com/watch?v=-Xj-7WBE7mw - reference video for gamma distributiion
#             2)https://towardsdatascience.com/how-to-generate-random-variables-from-scratch-no-library-used-4b71eb3c8dc7 - for poisson
#               and normal distribution
####################################################################################################
import random
random.seed(1000) #seeding
def ln(x): #for calculating log values
    n = 1000.0
    return n * ((x ** (1/n)) - 1)


def prob_5_6(dist): #problem 5.6 function to generate random numbers
    data = dist.split(",")
    index = 0
    p5_6 = []
    while(index < int(data[1])):
        if (random.random() < 0.8): #taking given probablitiy 0.8 for second machine
            p5_6.append((-1/(1/3))*(ln(1-random.random()))) #using 1/3 as lamda given in problem lamda = 20 min-1 => 60*1/20= 3
        else:
            p5_6.append((-1/(1/12))*(ln(1-random.random()))) #using 1/12 as lamda given in problem lamda = 5 min-1 => 60*1/5= 12
        index +=1
    print("Sample:",p5_6)
    mean_sd(p5_6) #generating Sample Mean and Sample Standard Deviation

def prob_5_1(dist):  #problem 5.6 function to generate random numbers
    data = dist.split(",")
    index = 0
    p5_1 = []
    while(index < int(data[1])):
        p5_1.append((random.random()) ** (2/3)) #by solving the give function and using inversion method we get (u)pow(2/3)
        index +=1

    print("Sample:",p5_1)
    mean_sd(p5_1)#generating Sample Mean and Sample Standard Deviation

def mean_sd(list):
    mean = 0
    for n in list: #calculating mean
        mean = n + mean

    mean = mean/len(list)

    sd = 0
    for n in list: #calculating Standard Deviation
        sd = (n - mean) ** 2 + sd

    sd = sd/(len(list) - 1)

    sd = sd ** (1/2)
    s1 = "Sample mean:"+ str(mean)
    s2 = "\nSample Standard Deviation:"+ str(sd)
    s3 = "\nSamples:"+ str(list)+"\n\n"
    f = open("result.txt", "w") #creation of file
    f.write(s1)
    f.write(s2)
    f.write(s3)
    f.close()

def arb_dis(dist): # Arbitrary distribution
    data = dist.split(",")
    index = 0
    i = 0
    p =[]
    abs = []
    for m in data:
        if(i > 2):
            p.append(float(m))
        i += 1
    i = 1
    p.sort()
    while(i < len(p)):
        p[i] += p[i-1]
        i +=1
    while(index < int(data[1])):
        u = random.random()
        i = 0
        while(i< len(p)-1):
            if(u <= p[i]):
                abs.append(int((u)))
                break
            i += 1
        index += 1

    print("Sample:",abs)
    mean_sd(abs)#generating Sample Mean and Sample Standard Deviation

def normal_dis(dist):#normal distribution
    data = dist.split(",")
    index = 0
    e = 2.71828
    nor = []
    while(index<int(data[1])):
        u1 = random.random()
        u2 = random.random()
        z0 = ((-2*ln(u1))**(1/2))*((e**((2*3.14159265359*u2)*(1j))).real)
        nor.append(z0*float(data[4])+float(data[3]))
        index +=1

    print("Sample:",nor)
    mean_sd(nor)#generating Sample Mean and Sample Standard Deviation

def gamma_dis(dist): # Gamma distribution
    data = dist.split(",")
    index = 0
    w = 0
    e = 2.71828
    gam = []
    while(index<int(data[1])):
        index += 1
        flag = True
        while(flag):
            if (float(data[3]) < 1): # if mean is less than one
                b = (e + float(data[3]))/e
                u1 = random.random()
                p = b*u1
                if(p <= 1):
                    y=p**(1/float(data[3]))
                    u2 = random.random()
                    if(u2 <= e**(-y)):
                        w = y
                        gam.append(w*float(data[4]))
                        flag = False
                        continue
                    else:
                        continue
                else:
                    y = -(ln((b-p)/float(data[3])))
                    u2 = random.random()
                    if u2 > (y**(float(data[3]) - 1)):
                        continue
                    else:
                        w = y
                        gam.append(w*float(data[4]))
                        flag = False
                        continue
            else:   #if mean is greater than 1
                a = 1/(((2*(float(data[3]))) - 1.0)**(1/2))
                b = float(data[3]) - ln(4)
                q = float(data[3]) + (1/a)
                d = 1 + ln(4.5)
                u1 = random.random()
                u2 = random.random()
                v = a * ln(u1/(1-u1))
                y = float(data[3]) * (e**v)
                z = (u1**2)*u2
                w = b + q*v - y
                if(w+d - (4.5)*z >= 0 ):
                    t = y
                    gam.append(t*float(data[4]))
                    flag = False
                    continue
                else:
                    if (w >= ln(z)):
                        t = y
                        gam.append(t*float(data[4]))
                        flag = False
                        continue
                    else:
                        continue
    print("Sample:",gam)
    mean_sd(gam)#generating Sample Mean and Sample Standard Deviation


def exponential_dis(dist): #exponential distribution
    data = dist.split(",")
    index = 0
    exp = []
    while(index<int(data[1])):
        exp.append((-1/float(data[3]))*(ln(1-random.random())))
        index +=1

    print("Sample:",exp)
    mean_sd(exp)

def poisson_dis(dist): #poisson distribution
    data = dist.split(",")
    index = 0
    index2 = 0
    k = 1
    e = 2.71828
    counter = 0
    counter2 = 0
    poss = []
    index2 = int(data[3])*5
    value = e ** (-int(data[3]))
    while(index < int(data[1])):
        rand_poss = []
        while(index2 > 1):
            rand_poss.append(random.random())
            index2 -=1
        while (k >= value ):
            k = rand_poss[counter] * k
            counter2 += 1
            counter += 1
        poss.append(counter2)
        counter2=0
        counter=0
        k=1
        index2 = int(data[3])*5
        index +=1
    print("Sample:",poss)

    mean_sd(poss)#generating Sample Mean and Sample Standard Deviation

def uniform_dis(dist): #uniform distribution
    data = dist.split(",")
    index = 0
    uni = []
    while(index <  int(data[1])):
        index += 1
        uni.append(int(data[3]) + (random.random() * (int(data[4]) - int(data[3]))))
    print("Sample:",uni)
    mean_sd(uni)#generating Sample Mean and Sample Standard Deviation

def neg_binom_dis(dist): #negative binomial distribution
    data = dist.split(",")
    p = float(data[4])
    q = 1 - p
    index = 0
    ber_list = []
    counter = 0
    k = int(data[3])
    succ = 0
    while(index < int(data[1])):
        while(succ != k):
            counter +=1
            if random.random() <= p:
                succ += 1
        succ = 0
        index += 1
        ber_list.append(counter)
        counter = 0
    print("Samples:",ber_list)
    mean_sd(ber_list)#generating Sample Mean and Sample Standard Deviation

def geometric_dis(dist): #geometric distribution
    data = dist.split(",")
    p = float(data[3])
    q = 1 - p
    index = 0
    ber_list = []
    counter = 0
    while(index < int(data[1])):
        counter += 1
        if random.random() <= p:
            ber_list.append(counter)
            index += 1
            counter = 0

    print("Samples:",ber_list)
    mean_sd(ber_list)#generating Sample Mean and Sample Standard Deviation

def binomial_dis(dist): #binomial distribution
    data = dist.split(",")
    p = float(data[4])
    q = 1 - p
    index = 0
    bino = 0
    counter = 0
    ber_list_a = []
    ber_list = []
    while(counter < int(data[1])):
        while(index < int(data[3])):
            index += 1
            if random.random() <= p:
                ber_list.append(1)
                bino += 1
            else:
                ber_list.append(0)
        counter += 1
        index = 0
        print("Samples",counter,":",ber_list, "=",bino)
        ber_list_a = ber_list_a + ber_list
        ber_list = []
        bino = 0
    mean_sd(ber_list_a)#generating Sample Mean and Sample Standard Deviation

def bernoulli_dis(dist): #bernoulli distribution
    data = dist.split(",")
    p = float(data[3])
    q = 1 - p
    index = 0
    ber = 0
    ber_list = []
    while(index < int(data[1])):
        index += 1
        if random.random() <= p:
            ber_list.append(1)
            ber += 1
        else:
            ber_list.append(0)

    print("Samples:",ber_list , "=",ber)
    mean_sd(ber_list)#generating Sample Mean and Sample Standard Deviation



def sampleGen(dist):
    data = dist.split(",")

    if int(data[0]) == 3:
        func = data[2]
        if func == "bernoulli":
            bernoulli_dis(dist)
        elif func == "binomial":
            binomial_dis(dist)
        elif func == "geometric":
            geometric_dis(dist)
        elif func == "uniform":
            uniform_dis(dist)
        elif func == "negative binomial":
            neg_binom_dis(dist)
        elif func == "poisson":
            poisson_dis(dist)
        elif func == "exponential":
            exponential_dis(dist)
        elif func == "gamma":
            gamma_dis(dist)
        elif func == "normal":
            normal_dis(dist)
        elif func == "arb":
            arb_dis(dist)
    elif int(data[0]) == 1:
        prob_5_1(dist)
    elif int(data[0]) == 2:
        prob_5_6(dist)

if __name__ == "__main__":

    dist = input("Problem number,Number of samples, distribution and parameters\n")
    sampleGen(dist)
