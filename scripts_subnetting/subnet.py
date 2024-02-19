import math

class network:
    def __init__(self, ip, sn_mask = 24): # ip and subnet mask (default /24)
        self.ip = ip
        self.sn_mask = sn_mask
 

    def sub_netting(self, nb_res):
    # add each sub-network and number of hosts in a dictionnary
        ss_res = {}
        nbh = 0
        for i in range(nb_res): # actions for each net
            if nbh > 2 ** (32 - self.sn_mask):
                return print("ce réseau ne peut pas accueillir autant d'hôtes.\nFin du programme.") # return error message if the number of hosts is too high
            else:
                sresi = int(input(f"nombre d'hôtes pour le réseau {i + 1}: ")) # input number of hosts
                ss_res[i + 1] = sresi # add number of hosts in the subnets dictionary
                nbh += sresi #

        ss_res = dict(sorted(ss_res.items(), key=lambda item: item[1], reverse=True))   # sort the dictionary by number of hosts in the sub-networks
       
        # keep the begining of the ip address
        res_ad = self.ip.split('.')
        debip = ''.join(f"{res_ad[i]}." for i in range(self.sn_mask//8))
    
        ipa = 0
        sub_r = {'réseau':[], 'ip':[], 'masque':[], '1e ip':[], 'dernier ip':[], 'ip broadcast':[]} # initialise dictionary with subnets parameters

        # calculate each parameter for each subnet
        for key, value in ss_res.items():
            pow = math.ceil(math.log(value + 2)/math.log(2))
            step = (2 ** pow) + 2
            sub_r['réseau'].append(str(key))
            sub_r['ip'].append(f"{debip}{str(ipa)}")
            sub_r['masque'].append(f"{'255.' * (int(self.sn_mask)//8)}{256 - (2 ** pow)}{'.0' * (3 - int(self.sn_mask)//8)}")
            sub_r['1e ip'].append(f"{debip}{ipa + 1}")
            sub_r['dernier ip'].append(f"{debip}{ipa + step - 4}")
            sub_r['ip broadcast'].append(f"{debip}{ipa + step - 3}")
            ipa += step - 2

        return sub_r



        
