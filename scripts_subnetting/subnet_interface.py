from multiprocessing.sharedctypes import Value
import subnet as sn

res_ad = input("adresse du réseau principal (ex: 192.168.0.1): ")
res_msr = int(input("masque de sous réseau du réseau principal (ex: /24) :/"))
nb_res = int(input("nombre de sous-réseaux à créer: "))

net = sn.network(res_ad, res_msr)
res = net.sub_netting(nb_res)

for i in range(nb_res):
    for key, value in res.items():
        print(f"{key}: ", value[i])
    print("\n")